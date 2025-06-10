# Изучите указанную страницу для получения информации о часах с четырёх страниц в разделе "ЧАСЫ".
# Вам потребуется заходить в каждую товарную карточку и собирать данные, отмеченные на предоставленном изображении.
# Сохраните данные в формате CSV с разделителем ;:
# delimiter=';'
# Отправьте ваш csv-файл на указанный валидатор. Обратите внимание на сохранение порядка строк и столбцов, так чтобы они соответствовали эталонному файлу.
# Если ваш файл совпадает с эталоном, вы получите код. Этот код нужно будет вставить в соответствующее поле.
# Для сравнения строк воспользуйтесь рекомендованным сервисом.

from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor


class DataSoup:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://parsinger.ru/html/"
        self.pagen_url = "https://parsinger.ru/html/index1_page_1.html"
        self.pagen_url_list = self.get_pagen()
        self.links = []
        self.links_executor = ThreadPoolExecutor(max_workers=10)
        self.all_zipped_data = []
        self.all_data_executor = ThreadPoolExecutor(max_workers=10)
        self.all_csv_data = []
        self.csv_file = "result.csv"
        self.columns = [
            "Наименование",
            "Артикул",
            "Бренд",
            "Модель",
            "Тип",
            "Технология экрана",
            "Материал корпуса",
            "Материал браслета",
            "Размер",
            "Сайт производителя",
            "Наличие",
            "Цена",
            "Старая цена",
            "Ссылка на карточку с товаром",
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

    def get_data_link(self, url):
        html = self.get_html(url)
        soup = BeautifulSoup(html, "lxml")

        data = soup.find_all(name="a", attrs={"class": "name_item"})

        result = [f"{self.base_url}{item.get("href")}" for item in data]

        self.links.extend(result)

    @staticmethod
    def split_data(string):
        key, value = string.split(":")
        if value:
            value = value.strip()

        return value

    def get_data(self, url):
        html = self.get_html(url)
        soup = BeautifulSoup(html, "lxml")

        data = soup.find(name="div", attrs={"class": "description"})

        p_header = data.find(name="p", attrs={"id": "p_header"}).get_text(strip=True)
        article = self.split_data(
            data.find(name="p", attrs={"class": "article"}).get_text(strip=True)
        )
        brand = self.split_data(
            data.find(name="ul", attrs={"id": "description"})
            .find(attrs={"id": "brand"})
            .get_text(strip=True)
        )
        model = self.split_data(
            data.find(name="ul", attrs={"id": "description"})
            .find(attrs={"id": "model"})
            .get_text(strip=True)
        )
        type = self.split_data(
            data.find(name="ul", attrs={"id": "description"})
            .find(attrs={"id": "type"})
            .get_text(strip=True)
        )
        display = self.split_data(
            data.find(name="ul", attrs={"id": "description"})
            .find(attrs={"id": "display"})
            .get_text(strip=True)
        )
        material_frame = self.split_data(
            data.find(name="ul", attrs={"id": "description"})
            .find(attrs={"id": "material_frame"})
            .get_text(strip=True)
        )
        material_bracer = self.split_data(
            data.find(name="ul", attrs={"id": "description"})
            .find(attrs={"id": "material_bracer"})
            .get_text(strip=True)
        )
        size = self.split_data(
            data.find(name="ul", attrs={"id": "description"})
            .find(attrs={"id": "size"})
            .get_text(strip=True)
        )
        site = self.split_data(
            data.find(name="ul", attrs={"id": "description"})
            .find(attrs={"id": "site"})
            .get_text(strip=True)
        )
        in_stock = self.split_data(
            data.find(attrs={"id": "in_stock"}).get_text(strip=True)
        )
        price = data.find(attrs={"id": "price"}).get_text(strip=True)
        old_price = data.find(attrs={"id": "old_price"}).get_text(strip=True)

        self.all_csv_data.append(
            [
                p_header,
                article,
                brand,
                model,
                type,
                display,
                material_frame,
                material_bracer,
                size,
                site,
                in_stock,
                price,
                old_price,
                url,
            ]
        )

    def run(self):
        with self.session:
            with self.links_executor as executor:
                futures = [
                    executor.submit(self.get_data_link, url)
                    for url in self.pagen_url_list
                ]

            with self.all_data_executor as executor:
                futures = [executor.submit(self.get_data, url) for url in self.links]

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
    ds.write_csv()

    end = time.perf_counter()

    print(f"Время выполнения: {end - start} секунд")


main()
