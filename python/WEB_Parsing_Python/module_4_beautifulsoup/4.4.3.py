# Когда вам необходимо найти тег по значению атрибута, в примере ниже value attr.
#
# <div name_attr="value attr">Информация в теге</div>
# Для того чтобы это сделать, необходимо воспользоваться именованным параметром attrs={}, который вы уже встречали в первом степе.
#
# soup.find(attrs={'name_attr': 'value attr'})
# Задача:
# Ваша задача — найти тег, который имеет имя и значение атрибута data-gpu="nVidia GeForce RTX 4060".
#
# Извлеките текст из тега после его нахождения.
#
# Ссылка на страницу c HTML.
#
# # В самом же задании необходимо изменить только одну строку, HTML уже вшит в степ.

from bs4 import BeautifulSoup
import requests

URL = "https://parsinger.ru/4.1/1/index3.html"


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
        data = self.soup.find(attrs={"data-gpu": "nVidia GeForce RTX 4060"})

        return data.text


def main():
    ds = DataSoup(URL)
    print(ds.get_data())


main()
