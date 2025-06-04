# Ваша задача — проанализировать страницу и понять как извлечь тег <img> целиком.
#
# У тега <img> есть только родитель и название тега. Найдите способ извлечь тег целиком.
#
# Пример извлеченного тега.
#
# <img src="images/Видеокарта MSI *** Bit Retail.jpg" alt="Видео *** Retail">
# Допишите функцию, изменив только одну строку.
#
# HTML вшит в задачу.

from bs4 import BeautifulSoup
import requests

URL = "https://parsinger.ru/4.1/1/index.html"


class DataSoup:
    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup(self.get_html(), "lxml")

    def get_html(self):
        response = requests.get(self.url)
        response.encoding = "utf-8"

        response.raise_for_status()

        if response.status_code == 200:
            return response.text
        else:
            return None

    def get_data(self):
        data = self.soup.find(name="img")

        return data


def main():
    ds = DataSoup(URL)
    print(ds.get_data())


main()
