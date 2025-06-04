# Проанализируйте страницу и найдите там тег с двойным классом description detailz
#
# Ваша задача — найти способ извлечь текст из этого тега.
#
# HTML страницы уже вшит в задание, вам необходимо изменить только код ниже.

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
        data = self.soup.find(attrs={"class": "description detailz"})

        return data.text


def main():
    ds = DataSoup(URL)
    print(ds.get_data())


main()
