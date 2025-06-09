# Откройте сайт на которой расположена таблица с объединёнными ячейками.
# Извлеките данные из каждой объединённой ячейки(всего 16 объединённых ячеек), объединённую ячейку можно определить по атрибуту colspan="n".
# Суммируйте все числовые значения, полученные из объединённых ячеек.
# Вставьте результат в поле ответа Степик.

from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor


class DataSoup:
    def __init__(self):
        self.session = requests.Session()
        self.url = "https://parsinger.ru/table/8/index.html"
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

            data = soup.find_all(attrs={"colspan": True})

            self.results = [int(item.get_text(strip=True)) for item in data]

    def sum(self):
        self.results.pop(0)

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
