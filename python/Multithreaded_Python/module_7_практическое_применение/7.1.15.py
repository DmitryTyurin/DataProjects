# Используйте библиотеки requests для отправки HTTP-запросов, BeautifulSoup для анализа HTML-контента.
# Напишите код для чтения файла, содержащего список URL-адресов, предположим, что файл называется generated_links.txt(он находится в архиве по ссылке выше).
# Для каждой ссылки из списка отправьте GET-запрос, чтобы получить содержимое веб-страницы. Используйте BeautifulSoup для извлечения всего текста со страницы.
# Подсчитайте количество слов на каждой рабочей странице.
# Убедитесь, что ваша программа корректно обрабатывает ошибки сети, недоступность страниц или любые другие исключения, чтобы не прерывать процесс анализа всех ссылок.
# Используйте ThreadPoolExecutor для ускорения процесса путем одновременной обработки нескольких ссылок.
# В конце работы программы вы должны получить количество слов, найденное на каждой странице, а также общее количество слов на всех страницах.
# Вставьте общее количество слов в поле ответа степик, в переменную result = <ваше значение> и нажмите кнопку отправить. print() использовать не нужно.
# P.S. Подумайте, потянет ли ваша система сразу такое количество запросов? Если нет, то стоит вспомнить про max_workers!

from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import requests

URL = "https://multithreading.ru/tasks/6.1/1/generated_links.txt"


class DataDownloader:
    def __init__(self):
        self.sum_words = 0
        self.executor = ThreadPoolExecutor(max_workers=10)

    @staticmethod
    def get_links_data(url: str):
        try:
            response = requests.get(url, verify=False)
            response.raise_for_status()

            return response.text
        except requests.exceptions.HTTPError as err:
            return None
        except Exception as err:
            return None

    @staticmethod
    def links_data_to_list(data: str):
        links = data.splitlines()

        return links

    @staticmethod
    def get_text_from_page(url: str):
        try:
            response = requests.get(url, verify=False)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text(separator=" ", strip=True)

            word_count = len(text.split())
            return word_count

        except requests.exceptions.HTTPError as err:
            return 0
        except Exception as err:
            return 0

    def get_sum_words(self, data: list):
        with self.executor as executor:
            futures = executor.map(self.get_text_from_page, data)

            for future in futures:
                if future:
                    self.sum_words += future
                else:
                    continue

        return self.sum_words


def main():
    downloader = DataDownloader()

    links_data = downloader.get_links_data(URL)
    links_data_list = downloader.links_data_to_list(links_data)

    sum_words = downloader.get_sum_words(links_data_list)
    print(sum_words)


main()
