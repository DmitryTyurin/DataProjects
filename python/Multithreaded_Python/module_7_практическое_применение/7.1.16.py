# Шаги выполнения задачи:
# Изучите папку с файлами, в каждом из которых находится по одной ссылке.
# Напишите функцию для чтения содержимого каждого файла в указанной директории. Функция должна извлекать URL-адрес, содержащийся в файле.
# Для каждой ссылки выполните HTTP-запрос. Используйте библиотеку requests для получения содержимого веб-страницы по URL.
# Используйте библиотеку BeautifulSoup для анализа HTML-страницы и поиска секретного кода. Секретный код находится внутри тега <div class="secret-code">. Извлеките текст из этого тега.
# Используйте ThreadPoolExecutor для параллельной обработки файлов.
# Выведите в консоль сообщение с секретным кодом, как только он будет найден.
# Вставьте полученный секретный код в поле ответа степик, в переменную secret_code. Использовать print() не нужно.
# P.S. Подумайте, потянет ли ваша система сразу такое количество запросов? Если нет, то стоит вспомнить про max_workers!

from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import zipfile
import os
import requests


class DataZipFile:
    def __init__(self, file_path: str, archive_name: str):
        self.file_path = file_path
        self.archive_name = archive_name
        self.executor = ThreadPoolExecutor(max_workers=10)
        self.results = []

    @staticmethod
    def read_txt_file(zip_ref, file_info):
        with zip_ref.open(file_info) as f:
            return f.read().decode("utf-8").strip()

    def process_archive(self):
        with zipfile.ZipFile(self.archive_name, "r") as zip_ref:
            txt_files = [f for f in zip_ref.infolist() if f.filename.endswith(".txt")]

            with self.executor as executor:
                futures = [
                    executor.submit(self.read_txt_file, zip_ref, file_info)
                    for file_info in txt_files
                ]

                for future in futures:
                    self.results.append(future.result())

        return self.results


class DataDownloader:
    def __init__(self):
        self.secret_words = []
        self.executor = ThreadPoolExecutor(max_workers=10)

    @staticmethod
    def get_text_from_page(url: str):
        try:
            response = requests.get(url, verify=False)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")
            secret_div = soup.find("div", {"class": "secret-code"})

            secret_code = secret_div.get_text().strip()
            return secret_code

        except requests.exceptions.HTTPError as err:
            return None
        except Exception as err:
            return None

    def get_secret_words(self, data: list):
        with self.executor as executor:
            results = executor.map(self.get_text_from_page, data)

            self.secret_words = [result for result in results if result is not None]

        return self.secret_words


def main():
    data_zip_file = DataZipFile(file_path=os.getcwd(), archive_name="files_6_1.zip")
    data_downloader = DataDownloader()

    links_results = data_zip_file.process_archive()
    secret_word = data_downloader.get_secret_words(links_results)

    print(secret_word)


main()
