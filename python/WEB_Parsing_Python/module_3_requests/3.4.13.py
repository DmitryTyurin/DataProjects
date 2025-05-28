# Цель задания:
# Научиться скачивать изображения с сайта с помощью Requests
#
# Условие:
# На сайт размещено 160 картинок.
# На одной из этих картинок, в углу, спрятан секретный код.
# Задачи:
# Напишите скрипт, который автоматически скачает все 160 изображений.
#
# После скачивания, просмотрите изображения вручную и найдите секретный код.
#
# Вставьте найденный код в поле для ответа на Степик.


import requests
from threading import Lock
from concurrent.futures import ThreadPoolExecutor

URL = "https://parsinger.ru/img_download"


class DataRequests:
    def __init__(self, url):
        self.url = url
        self.executor = ThreadPoolExecutor(max_workers=10)
        self.lock = Lock()

    def get_img(self, img_number: int):
        try:
            response = requests.get(
                f"{self.url}/img/ready/{img_number}.png", stream=True
            )
            response.raise_for_status()

            with open(f"png/{img_number}.png", "wb") as file:
                file.write(response.content)

            with self.lock:
                print(f"Загрузка {img_number}.png прошла успешно")
        except Exception as ex:
            print(ex)

    def run_get_img(self):
        import time

        start_time = time.perf_counter()

        with self.executor as executor:
            executor.map(self.get_img, range(1, 161))

        end_time = time.perf_counter()
        print(f"Загрузка изображений заняла: {round(end_time - start_time, 2)}")


dr = DataRequests(URL)
dr.run_get_img()
