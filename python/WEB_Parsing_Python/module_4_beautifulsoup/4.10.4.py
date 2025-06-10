# Используйте страницу чтобы собрать данные с четырёх страниц в категории hdd.
# "Проваливаться" в каждую карточку не нужно, соберите информацию с превью карточки.
# При создании CSV используйте разделитель:
# delimiter=';'
# Отправьте готовый csv файл в валидатор, для успешной валидации файла, необходимо сохранить тот же порядок строк и столбцов что и в эталонном файле.
# Если файл совпадает с эталонным на сервере, вы получите код который необходимо вставить в поле ответа.
# Используйте этот сервис для проверки разности строк.

from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor


class DataSoup:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://parsinger.ru/html/"
        self.pagen_url = "https://parsinger.ru/html/index4_page_1.html"
        self.pagen_url_list = self.get_pagen()
        self.get_data_executor = ThreadPoolExecutor(
            max_workers=len(self.pagen_url_list)
        )
        self.all_zipped_data = []
        self.all_csv_data = []
        self.csv_file = "result.csv"
        self.columns = [
            "Наименование",
            "Бренд",
            "Форм-фактор",
            "Ёмкость",
            "Объем буферной памяти",
            "Цена",
        ]
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

    def get_pagen(self):
        html = self.get_html(self.pagen_url)
        soup = BeautifulSoup(html, "lxml")

        data = soup.find(name="div", attrs={"class": "pagen"}).find_all(name="a")

        result = [f"{self.base_url}{item.get("href")}" for item in data]

        return result

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

    def run(self):
        with self.session:
            with self.get_data_executor as executor:
                futures = [
                    executor.submit(self.get_data, url) for url in self.pagen_url_list
                ]

    def transform_data(self):
        for name, price, description in self.all_zipped_data:
            brand, brand_value = description[0].split(":")
            form_facture, form_facture_value = description[1].split(":")
            capacity, capacity_value = description[2].split(":")
            volume, volume_value = description[3].split(":")

            brand_value = brand_value.strip()
            form_facture_value = form_facture_value.strip()
            capacity_value = capacity_value.strip()
            volume_value = volume_value.strip()

            self.all_csv_data.append(
                [
                    name,
                    brand_value,
                    form_facture_value,
                    capacity_value,
                    volume_value,
                    price,
                ]
            )

    def write_csv(self):
        import csv

        with open(self.csv_file, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file, delimiter=self.delimiter)
            writer.writerow(self.columns)

            for row in self.all_csv_data:
                writer.writerow(row)


def main():
    import time

    start = time.perf_counter()

    ds = DataSoup()

    ds.get_pagen()
    ds.run()
    ds.transform_data()
    ds.write_csv()

    end = time.perf_counter()

    print(f"Время выполнения: {end - start} секунд")


main()
