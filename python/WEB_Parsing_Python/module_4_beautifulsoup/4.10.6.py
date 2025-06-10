# Соберите указанные на изображении ниже данные с сайта тренажёра.
# Заходить в каждую карточку с товаром не требуется, собирать необходимо только с превью карточки.
# Сохраните данные в формате CSV с разделителем ;.
# delimiter=';'
# Отправьте ваш csv-файл на указанный валидатор. Обратите внимание на сохранение порядка строк и столбцов, так чтобы они соответствовали эталонному файлу.

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
        self.all_csv_data = []
        self.csv_file = "result.csv"
        self.delimiter = ";"

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
        if value:
            value = value.strip()

        return value

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
            brand_value = self.split_data(description[0])
            type_value = self.split_data(description[1])
            material_value = self.split_data(description[2])
            technology_value = self.split_data(description[3])

            self.all_csv_data.append(
                [
                    name,
                    brand_value,
                    type_value,
                    material_value,
                    technology_value,
                    price,
                ]
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

    def write_csv(self):
        import csv

        with open(self.csv_file, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file, delimiter=self.delimiter)

            for row in self.all_csv_data:
                writer.writerow(row)


def main():
    import time

    start = time.perf_counter()

    ds = DataSoup()
    ds.run()
    ds.transform_data()
    ds.write_csv()

    end = time.perf_counter()

    print(f"Время выполнения: {end - start} секунд")


main()
