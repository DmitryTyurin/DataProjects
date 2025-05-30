# Цель
# Целью этой задачи является определение первой и последней доступных страниц в заданном диапазоне URL-адресов.
#
# Условия
# # От
# https://parsinger.ru/3.3/4/1.html
#
# # До
# https://parsinger.ru/3.3/4/100.html
# Ваша задача сосредоточена на определении страниц с HTTP статус-кодом 200, который означает успешный ответ от сервера.
#
# Задачи
# Написать скрипт, который будет делать GET запросы к каждой странице в диапазоне.
#
# Определить, какая страница в диапазоне является первой доступной (статус-код 200).
#
# Определить, какая страница в диапазоне является последней доступной (также статус-код 200).
#
# Результат
# Программа должна вывести номера первой и последней доступных страниц в заданном диапазоне.
#
# Первая доступная страница: 3.html
# Последняя доступная страница: 98.html
# Проверяющая система Cтепик ожидает на проверку две строки как в примере выше, скопируйте их в свой код.
#
# Или используйте принты ниже.
#
# print(f"Первая доступная страница: {first_available_page}.html")
# print(f"Последняя доступная страница: {last_available_page}.html")


import requests
from threading import Lock
from concurrent.futures import ThreadPoolExecutor


class DataRequest:
    def __init__(self):
        self.url = "https://parsinger.ru/3.3/4/"
        self.status_code_list = []
        self.lock = Lock()
        self.executor = ThreadPoolExecutor(max_workers=100)

    def get_request(self, num_url):
        try:
            response = requests.get(f"{self.url}{num_url}.html")
            status_code = response.status_code

            if status_code == 200:
                self.status_code_list.append((num_url, status_code))

            with self.lock:
                print(f"{num_url}: {status_code}")
        except Exception as e:
            with self.lock:
                print(e)

    def create_executor(self):
        with self.executor as executor:
            futures = [executor.submit(self.get_request, i) for i in range(1, 101)]

    def get_interval(self):
        sorted_data = sorted(self.status_code_list, key=lambda x: x[0])

        first_available_page = sorted_data[0][0]
        last_available_page = sorted_data[-1][0]

        print(f"Первая доступная страница: {first_available_page}.html")
        print(f"Последняя доступная страница: {last_available_page}.html")

    def run(self):
        import time

        start_time = time.perf_counter()

        self.create_executor()
        self.get_interval()

        end_time = time.perf_counter()
        print(f"Время выполнения: {end_time - start_time} секунд")


data_request = DataRequest()
data_request.run()
