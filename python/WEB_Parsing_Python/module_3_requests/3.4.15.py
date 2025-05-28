# Задача:
# Напишите программу которая делает GET-запрос к указанной веб-странице для получения её HTML-кода.
# Выведите полученный HTML-код на экран с помощью response.text.
# Починить кодировку.
# Вставьте полученные HTML в поле ответа Степик.
# Структура HTML-кода страницы представлена в следующем виде:

import requests

URL = "https://parsinger.ru/3.4/2/index.html"


class DataRequests:
    def __init__(self, url):
        self.url = url

    def get_data(self):
        try:
            response = requests.get(self.url)

            if response.encoding != "utf-8":
                response.encoding = "utf-8"

            response.raise_for_status()

            return response.text

        except Exception as e:
            print(e)
            return None


dr = DataRequests(URL)
print(dr.get_data())
