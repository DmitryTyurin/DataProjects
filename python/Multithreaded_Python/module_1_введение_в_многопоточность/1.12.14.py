# Описание задачи:
#
# В вашем распоряжении находится словарь, содержащий 25 моделей самолетов и время их полета. Ваша задача - создать программу, которая запустит 25 потоков, соответствующих полету каждой модели самолета. Каждый поток будет имитировать полет продолжительностью, указанной в словаре.
#
# # Словарь с моделями самолетов и временем полета
# # Полный словарь вшит в задачу
#
# aircrafts = {
#     'Boeing 737': 6,
#     'Airbus A320': 9,
#     'Boeing 757': 2,
#     'Boeing 747': 6,
#     'Airbus A380': 7,
#     ...}
# Шаги выполнения задачи:
#
# Первым делом, ознакомьтесь со словарем aircrafts, где ключом является модель самолета (model), а значением - время его полета в секундах (flight_time).
#
# Создайте и запустите потоки для каждой модели самолета. Передайте в поток функцию flight_simulation, имя модели и время полета, как аргументы.
#
# Из функции flight_simulation() каждый поток должен выводить сообщение о начале полета, указывая модель самолета и время полета.
#
# # Пример сообщения:
# Boeing 737 начал полет. Время полета: 6 сек.
#
# print(f"{model} начал полет. Время полета: {flight_time} сек.")
#  Каждый поток после имитации полета заданной продолжительности должен выводить сообщение о завершении полета соответствующей модели самолета.
#
# # Пример сообщения:
# Boeing 737 завершил полет.
#
# print(f"{model} завершил полет.")
# Спустя 5 секунд после запуска всех потоков, программа должна вывести количество активных потоков, связанных с полетами самолетов, с помощью threading.active_count(). Это позволит анализировать, сколько самолетов еще находятся в "полете".
#
# print(f"Количество самолетов в воздухе после 5 секунд: {threading.active_count()}")
# P.S. Не упустите из виду тот факт, что в программе могут быть запущены потоки помимо тех 25, которые вы используете для имитации полетов!

import threading
import time

aircrafts = {
    "Boeing 737": 6,
    "Airbus A320": 9,
    "Boeing 757": 2,
}


class Flight:
    def __init__(self, aircrafts: dict):
        self.aircrafts = aircrafts
        self.threads = []

    @staticmethod
    def flight_simulation(model: str, flight_time: int | float) -> None:
        print(f"{model} начал полет. Время полета: {flight_time} сек.")
        time.sleep(flight_time)
        print(f"{model} завершил полет.")

    def start(self):
        for model, flight_time in self.aircrafts.items():
            thread = threading.Thread(
                target=self.flight_simulation, args=(model, flight_time)
            )
            self.threads.append(thread)
            thread.start()

        time.sleep(5)
        print(
            f"Количество самолетов в воздухе после 5 секунд: {threading.active_count() - 1}"
        )

        [thread.join() for thread in self.threads]


def main():
    flight = Flight(aircrafts)
    flight.start()


main()
