# Откройте сайт и найдите целевую таблицу.
# Для каждого столбца извлеките числа и вычислите их сумму.
# Округлите каждую сумму до трёх знаков после запятой.
# Сформируйте словарь, где ключи — названия столбцов, а значения — округлённые суммы.
# Вставьте словарь в поле ответа Степик в одну строку без переносов.

from bs4 import BeautifulSoup
import requests


class DataSoup:
    def __init__(self):
        self.session = requests.Session()
        self.url = "https://parsinger.ru/table/5/index.html"
        self.results = {}

    def get_html(self):
        try:
            response = self.session.get(self.url)
            response.encoding = "utf-8"
            response.raise_for_status()

            return response.text

        except requests.RequestException as e:
            print(f"Ошибка при запросе {self.url}: {e}")
            return None

    def sum_df_columns(self, df):
        for column in df.columns:
            self.results[column] = float(f"{df[column].sum():.3f}")

    def get_data(self):
        import pandas as pd
        from io import StringIO

        data = self.get_html()
        df = pd.read_html(StringIO(data))[0]

        self.sum_df_columns(df)

    def sum(self):
        return self.results


def main():
    ds = DataSoup()
    ds.get_data()
    print(ds.sum())


main()
