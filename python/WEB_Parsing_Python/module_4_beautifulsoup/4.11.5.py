# Соберите данные всех карточек товара всех категорий и со всех страниц тренажера
# (всего 160шт).
# Не "проваливайтесь" внутрь каждой карточки. Соберите только информацию из превью.
# Сохраните данные в JSON файл с использованием указанных параметров.
# json.dump(res, file, indent=4, ensure_ascii=False)
# Отправьте готовый JSON файл в валидатор, для успешной валидации файла, необходимо сохранить порядок объектов JSON:
# Порядок сбора категорий;
# Часы
# Телефоны
# Мыши
# HDD
# Наушники
# Имя файла произвольное.
# Удалите все лишние пробелы из данных. методом .strip().
# Если файл совпадает с эталоном на сервере, вы получите код. Этот код необходимо будет вставить в поле ответа.
# Используйте этот сервис для проверки разности строк.

from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor


class DataSoup:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://parsinger.ru/html/"
        self.pagen_url = "https://parsinger.ru/html/index1_page_1.html"
        self.pagen_list = []
        self.pagen_list_executor = ThreadPoolExecutor(max_workers=4)
        self.links = []
        self.links_executor = ThreadPoolExecutor(max_workers=10)
        self.all_zipped_data = []
        self.all_data_executor = ThreadPoolExecutor(max_workers=10)
        self.json_data = []
        self.json_file = "data"

    def get_html(self, url):
        try:
            response = self.session.get(url)
            response.encoding = "utf-8"
            response.raise_for_status()

            return response.text

        except requests.RequestException as e:
            print(f"Ошибка при запросе {url}: {e}")
            return None

    def get_pagen(self, pagen_url):
        html = self.get_html(pagen_url)
        soup = BeautifulSoup(html, "lxml")

        data = soup.find(name="div", attrs={"class": "pagen"}).find_all(name="a")

        result = [f"{self.base_url}{item.get("href")}" for item in data]

        self.pagen_list.extend(result)

    @staticmethod
    def split_data(string):
        key, value = string.split(":")

        if key:
            key = key.strip()
        if value:
            value = value.strip()

        return key, value

    def get_data(self, url):
        html = self.get_html(url)
        soup = BeautifulSoup(html, "lxml")

        data = soup.find_all(name="div", attrs={"class": "item"})

        name_item = [
            item.find(name="a", attrs={"class": "name_item"}).get_text(strip=True)
            for item in data
        ]

        description = [
            item.find(name="div", attrs={"class": "description"})
            .text.strip()
            .split("\n")
            for item in data
        ]

        price = [
            item.find(name="p", attrs={"class": "price"}).get_text(strip=True)
            for item in data
        ]

        zipped_data = zip(name_item, price, description)

        self.all_zipped_data.extend(zipped_data)

    def transform_data(self):
        for name, price, description in self.all_zipped_data:
            brand_key, brand_value = self.split_data(description[0])
            type_key, type_value = self.split_data(description[1])
            material_key, material_value = self.split_data(description[2])
            technology_key, technology_value = self.split_data(description[3])

            self.json_data.append(
                {
                    "Наименование": name,
                    brand_key: brand_value,
                    type_key: type_value,
                    material_key: material_value,
                    technology_key: technology_value,
                    "Цена": price,
                }
            )

    def run(self):
        with self.session:
            with self.pagen_list_executor as executor:
                [
                    executor.submit(
                        self.get_pagen,
                        f"https://parsinger.ru/html/index{i}_page_1.html",
                    )
                    for i in range(1, 6)
                ]

            with self.links_executor as executor:
                futures = [
                    executor.submit(self.get_data, url) for url in self.pagen_list
                ]

    def write_json(self):
        import json

        with open(self.json_file, "w", encoding="utf-8") as file:
            json.dump(self.json_data, file, indent=4, ensure_ascii=False)


def main():
    import time

    start = time.perf_counter()

    ds = DataSoup()
    ds.run()
    ds.transform_data()
    ds.write_json()

    end = time.perf_counter()

    print(f"Время выполнения: {end - start} секунд")


main()
