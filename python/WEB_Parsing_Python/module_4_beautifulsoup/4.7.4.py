# Цель: Посетить указанный веб-сайт и извлечь названия товаров со всех четырех страниц одной категории "МЫШИ". Необходимо организовать данные таким образом, чтобы названия товаров с каждой страницы хранились в отдельном списке. По завершении работы у вас должен быть главный список, содержащий четыре вложенных списка с названиями товаров.
#
# Условия выполнения:
#
# Посещение и анализ четырех страниц веб-сайта с пагинацией.
# Извлечение названий товаров с каждой страницы (8 шт на каждой странице).
# Сохранение названий товаров с каждой страницы в отдельном списке.
# Объединение всех четырех списков в один главный список.
# Метод strip() для названий товаров использовать не требуется.
# Отправьте полученый список списков в качестве ответа.

from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor


class DataSoup:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://parsinger.ru/html/"
        self.pagen_url = "https://parsinger.ru/html/index3_page_1.html"
        self.executor = ThreadPoolExecutor(max_workers=4)
        self.futures = []
        self.total_results = []

    def get_html(self, url):
        try:
            response = self.session.get(url)
            response.encoding = "utf-8"
            response.raise_for_status()

            return response.text

        except requests.RequestException as e:
            print(f"Ошибка при запросе {url}: {e}")
            return None

    def get_pagen(self):
        html = self.get_html(self.pagen_url)
        soup = BeautifulSoup(html, "lxml")

        data = soup.find(name="div", attrs={"class": "pagen"}).find_all(name="a")

        result = [f"{self.base_url}{item.get("href")}" for item in data]

        return result

    def get_data(self, url):
        html = self.get_html(url)
        soup = BeautifulSoup(html, "lxml")

        data = soup.find_all(name="a", attrs={"class": "name_item"})

        result = [item.get_text(strip=True) for item in data]

        self.total_results.append(result)

    def run(self):
        with self.session:
            pagen_list = self.get_pagen()

            with self.executor as executor:
                self.futures = [executor.map(self.get_data, pagen_list)]

        print(self.total_results)


def main():
    import time

    start = time.perf_counter()

    ds = DataSoup()
    ds.run()

    end = time.perf_counter()

    print(f"Время выполнения: {end - start}")


main()
