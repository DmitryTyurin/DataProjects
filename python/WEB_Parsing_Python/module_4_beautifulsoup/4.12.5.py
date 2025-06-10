# В данной задаче вы должны выполнить аналогичные действия, как и в предыдущей задаче, но с небольшим изменением. Вам необходимо определить, откуда приходят данные и в каком формате, а затем обработать эти данные следующим образом:
#
# Получение данных: Используйте инструменты разработчика для определения источника данных(вкладка Network). В нашем случае, данные лежат на этом веб-сайте.
# Обработка данных: Извлеките данные со страницы и создайте словарь, в котором для каждой карточки вычислите произведение значений "article" и "rating".
# Сбор значений: Суммируйте результаты произведений для каждой категории.
# Формирование словаря: Завершая задачу, создайте словарь, в котором ключами будут категории, а значениями - суммы произведений "article" и "rating".
# Вставьте полученный результат в поле для ответа.
# Пример словаря который нужно отправить на проверку.
#
# {'watch': 00000000000, 'mobile': 000000000000, 'mouse': 000000000000, 'hdd': 000000000000, 'headphones': 0000000000000}
# Напишите текст

from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor


class DataSoup:
    def __init__(self):
        self.session = requests.Session()
        self.url = "https://parsinger.ru/4.6/1/res.json"
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
            article = int(item.get("article"), 0)
            rating = int(item.get("description")["rating"])

            if categories in self.categories_count:
                self.categories_count[categories] += article * rating
            else:
                self.categories_count[categories] = article * rating

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
