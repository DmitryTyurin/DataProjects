# Открываем страницу сайта.
# Извлекаем при помощи bs4 данные о стоимости часов (всего 8 шт).
# Складываем все полученные числа.
# Вставляем результат в поле ответа.

from bs4 import BeautifulSoup
import requests

URL = "https://parsinger.ru/html/hdd/4/4_1.html"


class DataSoup:
    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup(self.get_html(), "lxml")
        self.total_sum = []

    def get_html(self):
        response = requests.get(self.url)
        response.encoding = "utf-8"

        response.raise_for_status()

        if response.status_code == 200:
            return response.text
        else:
            return None

    @staticmethod
    def extract_digits(text):
        import re

        pattern = r"\d{1,}\.\d{1,}|\d{1,}"
        digits = "".join(re.findall(pattern, text))

        return digits

    def get_books(self):
        data = self.soup.find("div", attrs={"class": "description"})

        return data

    def get_count(self, data, class_name):
        data = data.find(id=class_name)

        text_data = data.get_text(strip=True)
        text_data = self.extract_digits(text_data)
        int_data = int(text_data)

        return int_data

    def calculate_total_price(self):
        book_cards = self.get_books()

        price = self.get_count(book_cards, "price")
        old_price = self.get_count(book_cards, "old_price")

        sales = round((old_price - price) * 100 / old_price, 1)

        print(sales)


def main():
    ds = DataSoup(URL)
    ds.calculate_total_price()


main()
