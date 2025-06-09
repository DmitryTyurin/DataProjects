# Цель: Посетить указанный веб-сайт, систематически пройти по всем категориям, страницам и карточкам товаров (всего 160 шт.). Из каждой карточки товара извлечь стоимость и умножить ее на количество товара в наличии. Полученные значения агрегировать для вычисления общей стоимости всех товаров на сайте.
#
# Условия выполнения:
#
# Посещение и анализ всех категорий, страниц и карточек товаров на веб-сайте (всего 160 карточек товаров).
# Из каждой карточки извлечение стоимости товара и его количества в наличии.
# Умножение стоимости каждого товара на его количество в наличии.
# Суммирование всех полученных значений для вычисления общей стоимости всех товаров.
# Представление итоговой общей стоимости в качестве ответа.

from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor


class DataSoup:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://parsinger.ru/html/"
        self.pagen_list = []
        self.pagen_list_executor = ThreadPoolExecutor(max_workers=4)
        self.product_links = []
        self.product_links_executor = ThreadPoolExecutor(max_workers=10)
        self.product_data_executor = ThreadPoolExecutor(max_workers=10)
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

    def get_pagen(self, pagen_url):
        html = self.get_html(pagen_url)
        soup = BeautifulSoup(html, "lxml")

        data = soup.find(name="div", attrs={"class": "pagen"}).find_all(name="a")

        result = [f"{self.base_url}{item.get("href")}" for item in data]

        self.pagen_list.extend(result)

    def get_product_links(self, url):
        html = self.get_html(url)
        soup = BeautifulSoup(html, "lxml")

        data = soup.find_all(name="a", attrs={"class": "name_item"})

        result = [f"{self.base_url}{item.get("href")}" for item in data]

        self.product_links.extend(result)

    @staticmethod
    def extract_digits(text):
        import re

        pattern = r"\d{1,}\.\d{1,}|\d{1,}"
        digits = "".join(re.findall(pattern, text))

        return int(digits)

    def get_product_data(self, url):
        html = self.get_html(url)
        soup = BeautifulSoup(html, "lxml")

        stock = self.extract_digits(
            soup.find(attrs={"id": "in_stock"}).get_text(strip=True)
        )
        price = self.extract_digits(
            soup.find(attrs={"id": "price"}).get_text(strip=True)
        )

        result = [stock * price]

        self.total_results.extend(result)

    def run(self):
        with self.session:
            with self.pagen_list_executor as executor:
                [
                    executor.submit(
                        self.get_pagen,
                        f"https://parsinger.ru/html/index{i}_page_1.html",
                    )
                    for i in range(1, 6)
                ]

            with self.product_links_executor as executor:
                [
                    executor.submit(self.get_product_links, url)
                    for url in self.pagen_list
                ]

            with self.product_data_executor as executor:
                [
                    executor.submit(self.get_product_data, url)
                    for url in self.product_links
                ]

        print(sum(self.total_results))


def main():
    import time

    start = time.perf_counter()

    ds = DataSoup()
    ds.run()

    end = time.perf_counter()

    print(f"Время выполнения: {end - start} секунд")


main()
