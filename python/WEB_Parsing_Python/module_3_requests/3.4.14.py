# Цель задания:
# Закрепить навыки работы с методом response.json() при взаимодействии с API.
#
# Условие:
# Используйте API погодного сервиса, расположенный по адресу:
#
# API возвращает погодные данные для заданного города в формате JSON.
#
# Задача:
# Напишите код, который осуществляет GET-запрос к указанному API для получения погодных данных заданного города.
#
# Преобразовать полученный JSON-ответ в Python-объект с помощью метода response.json().
#
# Проанализировать данные и определить дату с самой минимальной температурой.
#
# Результат:
# Вставьте в поле для ответа дату с самой низкой температурой.
# Формат даты должен быть таким же, как в данных, полученных от API (например: 2023-10-01).


import requests
from threading import Lock
from concurrent.futures import ThreadPoolExecutor

URL = "https://parsinger.ru/3.4/1/json_weather.json"


class DataRequests:
    def __init__(self, url):
        self.url = url

    def get_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.json()

        except Exception as e:
            print(e)
            return None

    def get_min_date(self):
        data = self.get_data()

        for item in data:
            item["Температура воздуха"] = int(
                item["Температура воздуха"].replace("°C", "")
            )

        min_date = min(data, key=lambda x: x["Температура воздуха"])["Дата"]

        return min_date


dr = DataRequests(URL)
print(dr.get_min_date())
