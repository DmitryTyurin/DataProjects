# Ваша программа должна выводить список всех найденных на странице имен следующим образом.
# HTML страницы вшит в степ, вам необходимо изменить код ниже.
# P.S. "***" — это заместители текста строк, они вставлены, чтобы скрыть правильные ответы, их вставлять в ответ не нужно. Ваше решение должно вывести все найденные имена полностью!

from bs4 import BeautifulSoup
import requests

URL = "https://parsinger.ru/4.1/1/index4.html"


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
        data = self.soup.find_all(name="a", attrs={"class": "name_item product_name"})

        product_name = "\n".join([item.get_text(strip=True) for item in data])

        return product_name


def main():
    ds = DataSoup(URL)
    print(ds.get_data())


main()
