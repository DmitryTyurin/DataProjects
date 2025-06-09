# Ваш друг обратился к вам с просьбой помочь найти автомобиль, который соответствует определенным требованиям. Вы решили использовать ваши навыки программирования для написания кода, который может автоматически отфильтровать и сортировать автомобили по заданным критериям.
#
# Основные этапы выполнения задачи:
#
# Запрашивайте данные с веб-сайта, который содержит таблицу автомобилей.
# Фильтруйте автомобили по заданным критериям:
# Cтоимость не выше 4 000 000 (Стоимость авто <= 4000000),
# Год выпуска начиная с 2005 года (Год выпуска >= 2005),
# Тип двигателя - Бензиновый (Тип двигателя == "Бензиновый").

from bs4 import BeautifulSoup
import requests


class DataSoup:
    def __init__(self):
        self.session = requests.Session()
        self.url = "https://parsinger.ru/table/6/index.html"
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

    @staticmethod
    def filter_data(df):
        df = df.loc[
            (df["Стоимость авто"] <= 4000000)
            & (df["Год выпуска"] >= 2005)
            & (df["Тип двигателя"] == "Бензиновый")
        ]

        return df

    @staticmethod
    def sort_data(df):
        df = df.sort_values(by="Стоимость авто", ascending=True)

        df = df[["Марка Авто", "Год выпуска", "Тип двигателя", "Стоимость авто"]]

        return df

    def get_data(self):
        import pandas as pd
        from io import StringIO

        data = self.get_html()
        df = pd.read_html(StringIO(data))[0]

        filtered_df = self.filter_data(df)
        sorted_df = self.sort_data(filtered_df)

        return sorted_df

    @staticmethod
    def export_data(df):
        import json

        df_to_dict = df.to_dict(orient="records")

        return json.dumps(df_to_dict, indent=4, ensure_ascii=False)


def main():
    ds = DataSoup()
    df = ds.get_data()
    print(ds.export_data(df))


main()
