# Откройте сайт с шестью таблицами.
# Проверьте каждую ячейку всех таблиц на наличие чисел, кратных трём.
# Суммируйте все числа, кратные трём.
# Вставьте результат в поле ответа Степик.

from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor


class DataSoup:
    def __init__(self):
        self.session = requests.Session()
        self.url = "https://parsinger.ru/table/7/index.html"
        self.results = []

    def get_html(self):
        try:
            response = self.session.get(self.url)
            response.encoding = "utf-8"
            response.raise_for_status()

            return response.text

        except requests.RequestException as e:
            print(f"Ошибка при запросе {self.url}: {e}")
            return None

    def get_data(self):
        with self.session:
            soup = BeautifulSoup(self.get_html(), "html.parser")

            data = soup.find_all("td")

            self.results = [
                int(item.get_text(strip=True))
                for item in data
                if int(item.get_text(strip=True)) % 3 == 0
            ]

    def sum(self):
        return sum(self.results)


def main():
    import time

    start_time = time.perf_counter()

    ds = DataSoup()
    ds.get_data()
    print(ds.sum())

    end_time = time.perf_counter()

    print(f"Время выполнения: {end_time - start_time} сек")


main()
