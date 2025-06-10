# Вашей задачей является обработка данных в формате JSON, полученных по ссылке ​. Для подсчета общего количества товаров в разных категориях. Каждая карточка товара содержит информацию о количестве данного товара.
#
# Ожидаемый вывод:
# На выходе вашей программы должен быть словарь в одну строку в формате Python:
#
# {'watch': N, 'mobile': N, 'mouse': N, 'hdd': N, 'headphones': N}
# где N — это общее количество товаров для каждой категории.

from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor


class DataSoup:
    def __init__(self):
        self.session = requests.Session()
        self.url = "https://parsinger.ru/downloads/get_json/res.json"
        self.categories_count = {}

    def get_html(self):
        with self.session.get(self.url) as response:
            try:
                response.encoding = "utf-8"
                response.raise_for_status()

                return response.json()

            except requests.RequestException as e:
                print(f"Ошибка при запросе {self.url}: {e}")
                return None

    def get_data(self):
        import json

        data = self.get_html()

        for item in data:
            categories = item.get("categories")
            count = int(item.get("count"), 0)

            if categories in self.categories_count:
                self.categories_count[categories] += count
            else:
                self.categories_count[categories] = count

        if self.categories_count:
            return json.dumps(self.categories_count, ensure_ascii=False)
        else:
            return "Нет данных для обработки"


def main():
    import time

    start = time.perf_counter()

    ds = DataSoup()

    print(ds.get_data())

    end = time.perf_counter()

    print(f"Время выполнения: {end - start} секунд")


main()
