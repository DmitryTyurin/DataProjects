# Цель: моделирование гонки автомобилей, где все автомобили стартуют одновременно и по окончании гонки сообщают о своем финише.
#
# Задача:
#
# Используйте имя автомобиля из списка.
# car_models = ["Toyota", "BMW", "Audi", "Mercedes", "Ford", "Honda", "Nissan", "Chevrolet", "Volkswagen", "Kia"]  # Список моделей автомобилей
# Каждый автомобиль это отдельный поток.
# Используйте барьер для синхронизации старта гонки.
# Каждый автомобиль (поток) "едет" (выполняет работу) случайное время(не более 5 сек).
# По завершении "гонки" каждый автомобиль сообщает о своем  финише и сообщает время "гонки".
# print(f"Автомобиль {car_model} финишировал за {race_time:.2f} секунд")


from concurrent.futures import ThreadPoolExecutor
from threading import Barrier, Lock
import random
import time

car_models = [
    "Toyota",
    "BMW",
    "Audi",
    "Mercedes",
    "Ford",
    "Honda",
    "Nissan",
    "Chevrolet",
    "Volkswagen",
    "Kia",
]


class RacingCar:
    def __init__(self, car_model_list: list):
        self.car_model_list = car_model_list
        self.barrier: Barrier = Barrier(len(self.car_model_list))
        self.executor: ThreadPoolExecutor = ThreadPoolExecutor(
            max_workers=len(self.car_model_list)
        )
        self.lock: Lock = Lock()

    def race(self, car_model: str):
        race_time = random.uniform(1, 5)

        self.barrier.wait()

        time.sleep(race_time)

        with self.lock:
            print(f"Автомобиль {car_model} финишировал за {race_time:.2f} секунд")

    def start(self):
        with self.executor as executor:
            futures = executor.map(self.race, self.car_model_list)


race = RacingCar(car_models)
race.start()
