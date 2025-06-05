# Проанализируйте страницу и найдите способ извлечь все ID из каждого тега <li> (используйте select() или find_all()).
#
# HTML со страницы вшит в степ, вам осталось только изменить функцию ниже.
#
# Вывод ID должен происходить следующим образом.
#
# # По одному ID на строку
#
# item_1_brand
# item_1_card_type
# ***
# ***
# ***
# item_35_displayport
# item_35_power_pins
# P.S. "***" — в примере вывода вставлены для сокращения объема вывода и сокрытия реальных данных. В ваше решение их вставлять не нужно.

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
        data = self.soup.find_all(name="li")

        result = "\n".join([item.get("id") for item in data])

        return result


def main():
    ds = DataSoup(URL)
    print(ds.get_data())


main()
