# Проанализируйте структуру сайта, найдите способ получить все цены с помощью .find_all(), затем суммируйте их.
# HTML со страницы вшит в степ, вам осталось только изменить функцию ниже.

from bs4 import BeautifulSoup
import requests

URL = "https://parsinger.ru/4.1/1/index4.html"


class DataSoup:
    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup(self.get_html(), "lxml")
        self.all_prices = []

    def get_html(self):
        response = requests.get(self.url)
        response.encoding = "utf-8"

        response.raise_for_status()

        if response.status_code == 200:
            return response.text
        else:
            return None

    def get_data(self):
        import re

        data = self.soup.find_all(name="p", attrs={"class": "price product_price"})

        self.all_prices = [int(re.sub(r"\D", "", item.text)) for item in data]

        sum_prices = sum(self.all_prices)

        return sum_prices


def main():
    ds = DataSoup(URL)
    print(ds.get_data())


main()
