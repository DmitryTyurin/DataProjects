# Соберите данные о HDD с четырёх страниц в категории HDD.
# Не "проваливайтесь" внутрь каждой карточки. Соберите только информацию из превью.
# Сохраните данные в JSON файл с использованием указанных параметров.
# json.dump(res, file, indent=4, ensure_ascii=False)
# Отправьте готовый JSON файл в валидатор, для успешной валидации файла, необходимо сохранить тот же порядок объектов JSON (для этого необходимо собирать данные в том же порядке, в котором они находятся на сайте).
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
        self.pagen_url = "https://parsinger.ru/html/index4_page_1.html"
        self.pagen_url_list = self.get_pagen()
        self.get_data_executor = ThreadPoolExecutor(
            max_workers=len(self.pagen_url_list)
        )
        self.all_zipped_data = []
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

            self.json_data.append(
                {
                    "Наименование": name,
                    "Бренд": brand_value,
                    "Форм-фактор": form_facture_value,
                    "Ёмкость": capacity_value,
                    "Объем буферной памяти": volume_value,
                    "Цена": price,
                }
            )

    def write_json(self):
        import json

        with open(self.json_file, "w", encoding="utf-8") as file:
            json.dump(self.json_data, file, indent=4, ensure_ascii=False)


def main():
    import time

    start = time.perf_counter()

    ds = DataSoup()

    ds.get_pagen()
    ds.run()
    ds.transform_data()
    ds.write_json()

    end = time.perf_counter()

    print(f"Время выполнения: {end - start} секунд")


main()
