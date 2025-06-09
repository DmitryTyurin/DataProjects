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

    def is_multiple_of_three(self, df):
        for col in df.columns:
            for val in df[col]:
                num = int(val)
                if num % 3 == 0:
                    self.results.append(num)

    def get_data(self, index):
        import pandas as pd
        from io import StringIO

        data = self.get_html()
        df = pd.read_html(StringIO(data))[index]

        self.is_multiple_of_three(df)

    def run_executor(self):
        with self.session:
            soup = BeautifulSoup(self.get_html(), "html.parser")

            all_tables_list = [
                item.get_text(strip=True) for item in soup.find_all(name="thead")
            ]

            len_all_tables_list = len(all_tables_list)

            with ThreadPoolExecutor(max_workers=len_all_tables_list) as executor:
                futures = [
                    executor.submit(self.get_data, index)
                    for index in range(len_all_tables_list)
                ]

    def sum(self):
        return sum(self.results)


def main():
    import time

    start_time = time.perf_counter()

    ds = DataSoup()
    ds.run_executor()
    print(ds.sum())

    end_time = time.perf_counter()

    print(f"Время выполнения: {end_time - start_time} сек")


main()
