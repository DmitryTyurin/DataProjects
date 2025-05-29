# Цель:
# Вашей задачей является создание скрипта, который делает сетевые запросы к указанному диапазону ссылок для выявления единственной рабочей страницы и поиска кода на ней. Для этого необходимо считывать HTTP статус-код каждой страницы.
#
# Диапазон ссылок:
# # От
# https://parsinger.ru/3.3/1/1.html
#
# # До
# https://parsinger.ru/3.3/1/200.html
# Детали:
# В указанном диапазоне существует только одна рабочая страница с HTTP статус-кодом 200 (OK).
# Все остальные страницы возвращают HTTP статус-код 404 (Not Found).
# Задание:
# Выполните HTTP запрос к каждой ссылке в заданном диапазоне.
# Считывайте HTTP статус-код каждой страницы.
# Определите, какая именно ссылка является рабочей, то есть возвращает HTTP статус-код 200 (OK).
# Перейдите по рабочей ссылке вручную, или получите данные с помощью response.text для извлечения числа на этой странице.
# Вставьте число в поле ответа Cтепик.


import requests
from threading import Lock
from concurrent.futures import ThreadPoolExecutor


class DataRequest:
    def __init__(self):
        self.url = "https://parsinger.ru/3.3/1/"
        self.text_list = []
        self.lock = Lock()
        self.executor = ThreadPoolExecutor(max_workers=100)

    def get_request(self, num_url):
        try:
            response = requests.get(f"{self.url}{num_url}.html")
            response.raise_for_status()

            if response.status_code == 200:

                if response.encoding != "utf-8":
                    response.encoding = "utf-8"

                self.text_list.append(response.text)

        except Exception as e:
            with self.lock:
                print(e)

    def create_executor(self):
        with self.executor as executor:
            futures = [executor.submit(self.get_request, i) for i in range(1, 201)]

    def print_text(self):
        print(" ".join(self.text_list))

    def run(self):
        import time

        start_time = time.perf_counter()

        self.create_executor()
        self.print_text()

        end_time = time.perf_counter()
        print(f"Время выполнения: {end_time - start_time} секунд")


data_request = DataRequest()
data_request.run()
