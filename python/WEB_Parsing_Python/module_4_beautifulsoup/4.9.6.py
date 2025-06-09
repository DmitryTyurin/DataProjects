# Перейдите на сайт и найдите целевую таблицу.
# Выполните парсинг таблицы, извлекая числа из ячеек, содержащих форматирование с тегом (используйте .find('b') или .find_all('b'))
# Соберите все числа из выделенных ячеек, исключая данные заголовка таблицы.
# Рассчитайте сумму извлечённых чисел.
# Вставьте результат в поле ответа в формате числа с плавающей точкой.

from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor


class DataSoup:
    def __init__(self):
        self.session = requests.Session()
        self.url = "https://parsinger.ru/table/3/index.html"
        self.results = []

    def get_html(self):
        try:
            response = self.session.get(self.url)
            response.encoding = "utf-8"
            response.raise_for_status()

            return response.text

        except requests.RequestException as e:
            print(f"Ошибка при запросе {self.url}: {e}")
            return None

    def get_data(self):
        html = self.get_html()
        soup = BeautifulSoup(html, "lxml")

        data = soup.find_all("b")

        self.results = [float(i.text) for i in data]

    def sum(self):
        return sum(self.results)


def main():
    ds = DataSoup()
    ds.get_data()
    print(sum(ds.results))


main()
