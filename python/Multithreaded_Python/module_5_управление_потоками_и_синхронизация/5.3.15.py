# Цель: Симулировать аукцион, где участники (потоки) делают ставки на предметы. Аукцион начинается после сигнала от аукциониста.
#
# Задача:
#
# Аукцион начинается с оповещения о начале.
# # Старт аукциона
# print("Аукцион начинается!")
#
# Аукцион начинается!
# Создать несколько потоков, каждый из которых представляет участника аукциона.
# # Имена участников аукциона
# bidder_names = ["Сергей", "Борис", "Виктор", "Евдоким", "Егор"]
# Участники ожидают начала аукциона выводя сообщение о готовности.
# Участник Сергей готов к аукциону.
# print(f"Участник {name} готов к аукциону.")
# По сигналу аукциониста (главный поток устанавливает событие) аукцион начинается, и участники начинают делать ставки.
# Участник Сергей делает ставку на редкую картину.
# print(f"Участник {name} делает ставку на редкую картину.")

from concurrent.futures import ThreadPoolExecutor
import threading
import time
import random

bidder_names = ["Сергей", "Борис", "Виктор", "Евдоким", "Егор"]


class ProcessBidder:
    def __init__(self, name: list):
        self.name = name
        self.event = threading.Event()
        self.executor = ThreadPoolExecutor(max_workers=len(self.name))
        self.bet = random.randint(1, 3)

    def bidder(self, name: str):
        print(f"Участник {name} готов к аукциону.")

        self.event.wait()

        print(f"Участник {name} делает ставку на редкую картину.")

    def run(self):
        print("Аукцион начинается!")

        with self.executor as executor:
            futures = executor.map(self.bidder, bidder_names)

            self.event.set()


process = ProcessBidder(bidder_names)
process.run()
