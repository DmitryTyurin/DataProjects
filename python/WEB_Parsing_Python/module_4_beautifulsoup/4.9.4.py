# Перейдите на сайт и найдите целевую таблицу.
#
# Выполните парсинг данных из таблицы.
#
# Извлеките все уникальные числа из ячеек таблицы, исключая числа, содержащиеся в заголовке.
#
# Рассчитайте сумму извлечённых уникальных чисел.
# Вставьте результат в поле ответа в формате числа с плавающей точкой (например, ***.0959999999998)
#
# Вставить полученный результат в поле ответа Степик.

from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor


class DataSoup:
    def __init__(self):
        self.session = requests.Session()
        self.url = "https://parsinger.ru/table/1/index.html"
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

    def unique_numbers(self, df):
        import pandas as pd

        for column in df.columns:
            unique_values = df[column].drop_duplicates().tolist()

            self.results.extend(unique_values)

    def get_data(self):
        import pandas as pd
        from io import StringIO

        data = self.get_html()

        df = pd.read_html(StringIO(data))[0]
        self.unique_numbers(df)

    def sum(self):
        set_results = set(self.results)

        return sum(set_results)


def main():
    ds = DataSoup()
    ds.get_data()
    print(ds.sum())


main()
