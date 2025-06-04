# Когда у тега нет класса, но есть пользовательский атрибут, вы можете использовать синтаксис:
#
# soup.find('tag', {'data-attribute': 'value'})
# Задача:
# Допишите код ниже, чтобы найти  необходимый тег из встроенного в степ HTML.
#
# Найдите тег <li> который имеет имя атрибута data-key и значение атрибута cooling_system.
#
# Извлеките текст из тега.
#
# Ссылка на страницу c HTML.

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
        data = self.soup.find(name="li", attrs={"data-key": "cooling_system"})

        return data.text


def main():
    ds = DataSoup(URL)
    print(ds.get_data())


main()
