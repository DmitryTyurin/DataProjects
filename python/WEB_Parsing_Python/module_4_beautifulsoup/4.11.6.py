# Соберите данные из категории mobile  (всего 32 карточки).
# "Провалитесь" в каждую карточку и соберите необходимую информацию.
# Сохраните данные в JSON файл с использованием указанных параметров.
# json.dump(res, file, indent=4, ensure_ascii=False)
# Отправьте готовый JSON файл в валидатор, для успешной валидации файла, необходимо сохранить порядок объектов JSON:
# Ключи словаря должны быть собраны из id в тегах  li;
#
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
        self.pagen_url = "https://parsinger.ru/html/index2_page_1.html"
        self.pagen_url_list = self.get_pagen()
        self.links = []
        self.links_executor = ThreadPoolExecutor(max_workers=10)
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

    def get_description(self, data, description_id):
        return self.split_data(
            data.find(name="ul", attrs={"id": "description"})
            .find(attrs={"id": description_id})
            .get_text(strip=True)
        )

    def get_data(self, url):
        html = self.get_html(url)
        soup = BeautifulSoup(html, "lxml")

        data = soup.find(name="div", attrs={"class": "description"})
        description = data.find("ul", id="description").find_all("li")

        p_header = data.find(name="p", attrs={"id": "p_header"}).get_text(strip=True)
        article = self.split_data(
            data.find(name="p", attrs={"class": "article"}).get_text(strip=True)
        )

        description_dict = dict(
            zip(
                [x["id"] for x in description],
                [
                    self.get_description(data, "brand"),
                    self.get_description(data, "model"),
                    self.get_description(data, "type"),
                    self.get_description(data, "material"),
                    self.get_description(data, "type_display"),
                    self.get_description(data, "diagonal"),
                    self.get_description(data, "size"),
                    self.get_description(data, "weight"),
                    self.get_description(data, "resolution"),
                    self.get_description(data, "site"),
                ],
            )
        )

        in_stock = self.split_data(
            data.find(attrs={"id": "in_stock"}).get_text(strip=True)
        )
        price = data.find(attrs={"id": "price"}).get_text(strip=True)
        old_price = data.find(attrs={"id": "old_price"}).get_text(strip=True)

        self.json_data.append(
            {
                "categories": "mobile",
                "name": p_header,
                "article": article,
                "description": description_dict,
                "count": in_stock,
                "price": price,
                "old_price": old_price,
                "link": url,
            }
        )

    def run_executor(self):
        with self.session:
            with self.links_executor as executor:
                futures = [
                    executor.submit(self.get_data_link, url)
                    for url in self.pagen_url_list
                ]

            with self.all_data_executor as executor:
                futures = [executor.submit(self.get_data, url) for url in self.links]

    def write_json(self):
        import json

        with open(self.json_file, "w", encoding="utf-8") as file:
            json.dump(self.json_data, file, indent=4, ensure_ascii=False)


def main():
    import time

    start = time.perf_counter()

    ds = DataSoup()

    ds.get_pagen()
    ds.run_executor()
    ds.write_json()

    end = time.perf_counter()

    print(f"Время выполнения: {end - start} секунд")


main()
