# Напишите программу для симуляции работы кафе. У вас есть два потока - один представляет посетителей кафе, а другой - баристу, который готовит кофе. Посетители должны ожидать своего заказа, а бариста должен готовить кофе. Когда бариста заканчивает приготовление кофе, он оповещает посетителя, который забирает свой заказ. После того как все посетители получили свой кофе, программа должна завершиться с выводом в консоль:
#
# Все посетители получили свой кофе. Работа завершена.
# Имейте в виду, что приготовление кофе занимает 2 секунды, и после приготовления баристе нужно прибрать рабочее место (1 секунда), прежде чем он приступит к обслуживанию следующего клиента.
#
# Попробуйте реализовать данную задачу, используя парадигму ООП.
#
# Используйте следующий список посетителей кофейни:
#
# ["Алиса", "Владимир", "Сергей"]

from concurrent.futures import ThreadPoolExecutor
from threading import Condition, Event
import time
from queue import Queue


class CoffeeShop:
    def __init__(self):
        self.customers: list = ["Алиса", "Владимир", "Сергей"]
        self.condition: Condition = Condition()
        self.executor: ThreadPoolExecutor = ThreadPoolExecutor(
            max_workers=len(self.customers)
        )

    def visit_customer(self, customer: str):
        with self.condition:
            print(f"{customer} зашел в кафе")

            self.condition.wait()

            print(f"{customer} получил свой кофе")

    def barista(self):
        for customer in self.customers:
            with self.condition:
                print(f"Готовим кофе для {customer}")
                time.sleep(2)
                print(f"Кофе для {customer} готов")

                self.condition.notify()
                time.sleep(1)

    def run(self):
        with self.executor as executor:
            visit_customer_futures = executor.map(self.visit_customer, self.customers)

            with self.condition:
                self.condition.notify_all()

            barista_future = executor.submit(self.barista)

        print("Все посетители получили свой кофе. Работа завершена.")


shop = CoffeeShop()
shop.run()
