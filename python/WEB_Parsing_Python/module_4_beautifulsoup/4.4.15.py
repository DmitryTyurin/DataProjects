# Проанализируйте HTML на странице и извлеките из него текст находящийся после третьего раздела.
# HTML уже вшит в задачу, вам необходимо изменить только функцию ниже.
# Используйте функцию strip() для удаления лишних пробелов.

from bs4 import BeautifulSoup
import requests

URL = "https://parsinger.ru/4.1/1/index6.html"


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

        data = self.soup.find(
            name="p", attrs={"class": "section-text"}, string="Текст раздела 3"
        )
        next_data = data.next_sibling
        next_data = next_data.get_text(strip=True)

        return next_data


def main():
    ds = DataSoup(URL)
    print(ds.get_data())


main()
