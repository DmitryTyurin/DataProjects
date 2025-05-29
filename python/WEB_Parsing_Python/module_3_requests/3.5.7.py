# Вашей задачей является написание кода, который будет выполнять сетевые запросы к указанному диапазону веб-страниц и суммировать HTTP статус-коды всех полученных ответов.
#
# # От
# https://parsinger.ru/3.3/2/1.html
#
# # До
# https://parsinger.ru/3.3/2/200.html
# Примерно половина ссылок в этом диапазоне возвращает HTTP статус-код 200 (OK).
# Оставшаяся половина возвращает HTTP статус-код 404 (Not Found).
# Задание:
# Сделайте HTTP запрос к каждой странице в указанном диапазоне.
# Получите HTTP статус-код каждой страницы.
# Суммируйте все полученные статус-коды.
# Ожидаемый результат:
# В качестве результата вы должны получить общую сумму всех HTTP статус-кодов, полученных от всех страниц в указанном диапазоне.
#
# Примечание:
# Учтите, что задача предполагает обработку большого числа HTTP запросов. Обдумайте, как можно оптимизировать ваш код для минимизации времени выполнения.


import requests
from threading import Lock
from concurrent.futures import ThreadPoolExecutor


class DataRequest:
    def __init__(self):
        self.url = "https://parsinger.ru/3.3/2/"
        self.status_code_list = []
        self.lock = Lock()
        self.executor = ThreadPoolExecutor(max_workers=100)

    def get_request(self, num_url):
        try:
            response = requests.get(f"{self.url}{num_url}.html")
            status_code = response.status_code

            self.status_code_list.append(status_code)

            with self.lock:
                print(f"{num_url}: {status_code}")
        except Exception as e:
            print(e)

    def create_executor(self):
        with self.executor as executor:
            futures = [executor.submit(self.get_request, i) for i in range(1, 201)]

    def print_sum(self):
        if self.status_code_list:
            print(f"Сумма статус-кодов: {sum(self.status_code_list)}")
        else:
            print("Нет статус-кодов")

    def run(self):
        import time

        start_time = time.perf_counter()

        self.create_executor()
        self.print_sum()

        end_time = time.perf_counter()
        print(f"Время выполнения: {end_time - start_time} секунд")


data_request = DataRequest()
data_request.run()
