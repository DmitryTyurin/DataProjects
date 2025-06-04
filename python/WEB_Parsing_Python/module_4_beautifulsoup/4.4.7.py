# Задача:
# Ваша задача заключается в поиске тега который содержит сразу все перечисленные ниже атрибуты и значения.
#
# class="description_detail class1 class2 class3"
# data-fdg45="value13"
# data-54dfg60="value14"
# data-d6f50hg="value15"
# После того как тег будет найден, извлеките из него текст.
#
# Ссылка на страницу с необходимым HTML.
#
# Этот HTML уже вшит в задание, и вам необходимо только изменить код ниже.

from bs4 import BeautifulSoup
import requests

URL = "https://parsinger.ru/4.1/1/index2.html"


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
        data = self.soup.find(
            attrs={
                "class": "description_detail class1 class2 class3",
                "data-fdg45": "value13",
                "data-54dfg60": "value14",
                "data-d6f50hg": "value15",
            }
        )

        return data.text


def main():
    ds = DataSoup(URL)
    print(ds.get_data())


main()
