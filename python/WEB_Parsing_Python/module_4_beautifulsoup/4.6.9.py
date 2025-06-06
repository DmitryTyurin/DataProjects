# Открываем страницу сайта.
# Извлекаем при помощи bs4 данные о стоимости часов (всего 8 шт).
# Складываем все полученные числа.
# Вставляем результат в поле ответа.

from bs4 import BeautifulSoup
import requests

URL = "https://parsinger.ru/html/index1_page_1.html"


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
        data = self.soup.find_all("div", attrs={"class": "item_card"})

        return data

    def get_count(self, data, class_name):
        data = data.find_all("p", attrs={"class": class_name})

        for i in data:
            text_data = i.get_text(strip=True)
            text_data = self.extract_digits(text_data)
            text_data = int(text_data)

            self.total_sum.append(text_data)

    def calculate_total_price(self):
        book_cards = self.get_books()

        for card in book_cards:
            self.get_count(card, "price")

        print(sum(self.total_sum))


def main():
    ds = DataSoup(URL)
    ds.calculate_total_price()


main()
