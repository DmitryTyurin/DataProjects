# Цель: Посетить указанный веб-сайт, пройти по всем страницам в категории "мыши" и из каждой карточки товара извлечь артикул. После чего все извлеченные артикулы необходимо сложить и представить в виде одного числа.
#
# Условия выполнения:
#
# Посещение и анализ всех страниц в категории "МЫШИ" на веб-сайте (всего 4 страницы).
# Переход в каждую карточку товара на каждой странице категории "МЫШИ" (всего 32 товара).
# Используя библиотеку bs4, извлечение артикула из каждой карточки товара
# (например, из элемента <p class="article">Артикул: 80244813</p>).
# Сложение всех извлеченных артикулов.
# Представление полученного результата в качестве ответа.

from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor


class DataSoup:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://parsinger.ru/html/"
        self.pagen_url = "https://parsinger.ru/html/index3_page_4.html"
        self.pagen_executor = ThreadPoolExecutor(max_workers=4)
        self.mouse_links = []
        self.mouse_executor = ThreadPoolExecutor(max_workers=10)
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

    def get_mouse_links(self, url):
        html = self.get_html(url)
        soup = BeautifulSoup(html, "lxml")

        data = soup.find_all(name="a", attrs={"class": "name_item"})

        result = [f"{self.base_url}{item.get("href")}" for item in data]

        self.mouse_links.extend(result)

    @staticmethod
    def extract_digits(text):
        import re

        pattern = r"\d{1,}\.\d{1,}|\d{1,}"
        digits = "".join(re.findall(pattern, text))

        return int(digits)

    def get_mouse_data(self, url):
        html = self.get_html(url)
        soup = BeautifulSoup(html, "lxml")

        data = soup.find(name="p", attrs={"class": "article"})

        result = [self.extract_digits(item.get_text(strip=True)) for item in data]

        self.total_results.extend(result)

    def run(self):
        with self.session:
            pagen_list = self.get_pagen()

            with self.pagen_executor as executor:
                [executor.submit(self.get_mouse_links, url) for url in pagen_list]

            with self.mouse_executor as executor:
                [executor.submit(self.get_mouse_data, url) for url in self.mouse_links]

        print(sum(self.total_results))


def main():
    import time

    start = time.perf_counter()

    ds = DataSoup()
    ds.run()

    end = time.perf_counter()

    print(f"Время выполнения: {end - start} секунд")


main()
