# Откройте сайт и найдите целевую таблицу.
# Для каждой строки таблицы извлеките числа из оранжевой и голубой ячеек и умножьте их.
# Рассчитайте сумму всех полученных произведений.
# Вставьте результат в поле ответа Степик в формате числа с плавающей точкой (например, ******.456**)

from bs4 import BeautifulSoup
import requests


class DataSoup:
    def __init__(self):
        self.session = requests.Session()
        self.url = "https://parsinger.ru/table/5/index.html"
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

    def get_orange_data(self):
        html = self.get_html()
        soup = BeautifulSoup(html, "lxml")

        orange_data = soup.find_all(attrs={"class": "orange"})
        orange_cells = [float(cell.text) for cell in orange_data]

        return orange_cells

    def get_blue_data(self):
        import pandas as pd
        from io import StringIO

        data = self.get_html()

        df = pd.read_html(StringIO(data))[0]
        df = df.iloc[:, -1].to_list()

        return df

    def sum(self):
        orange_data = self.get_orange_data()
        blue_data = self.get_blue_data()

        zipped_data = zip(orange_data, blue_data)
        self.results = [x * y for x, y in zipped_data]

        return sum(self.results)


def main():
    ds = DataSoup()
    print(ds.sum())


main()
