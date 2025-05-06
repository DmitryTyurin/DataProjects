# Ваша задача — моделирование работы ресторана, где заказы клиентов (задачи) обрабатываются поварами (рабочими потоками). Официант (главный поток) распределяет заказы по поварам. Повара ожидают заказы и начинают готовить блюда, как только заказы поступают. Используйте threading.Condition для синхронизации между официантом и поварами.
#
# Детали:
#
# Официант получает список заказов от клиентов и помещает их в очередь.
# # Список официантов
# waiters = ["Анна", "Иван", "Света"]
# Повара ожидают заказы и начинают готовить их по мере поступления.
# # Список поваров
# chefs = ["Шеф_Антон", "Шеф_Сергей", "Шеф_Георгий"]
# Список блюд.
# # Список блюд
# dishes = ["Борщ", "Салат Цезарь", "Стейк", "Паста Карбонара", "Тирамису"]
#
#
# Используйте списки имен для официантов (waiters), поваров (chefs) и блюд (dishes).
# Используйте потоки для имитации одновременной работы официантов и поваров.
# Синхронизируйте действия между официантами и поварами, используя  Condition() .
# Функция официанта waiter():
#
# Каждый официант должен принять фиксированное количество заказов(3).
# Каждый официант должен принимать заказ от 1 сек до 3 сек.
# Для каждого заказа официант выбирает случайное блюдо из списка dishes=[].
# Используйте condition для синхронизации и уведомления поваров о новых заказах.
# Функция официанта должна выводить следующее сообщение:
# Иван передал заказ на Паста Карбонара
#
# print(f"{waiter_name} передал заказ на {dish}")
# Функция повара chef():
#
# Повар берёт заказы для приготовления.
# Повар ожидает новых заказов.
# Каждый повар выполняет заказ от 1 сек до 3 сек.
# После обработки всех заказов и получения уведомления о завершении, повар завершает свою работу.
# Повар должен выводить следующие сообщения.
# Шеф_Сергей готовит Паста Карбонара...
# print(f"{chief_name} готовит {dish}...")
#
# # и
#
# Шеф_Сергей закончил готовить Паста Карбонара
# print(f"{chief_name} закончил готовить {dish}")
# Запуск и синхронизация потоков:
#
# Создайте и запустите отдельные потоки для каждого официанта и повара.
# Дождитесь завершения работы всех официантов, затем  уведомите поваров.
# После уведомления, дождитесь завершения работы всех поваров.

from concurrent.futures import ThreadPoolExecutor
from threading import Thread, Condition
from queue import Queue
import random
import time


class RestaurantService:
    def __init__(self):
        self.waiters = ["Анна", "Иван", "Света"]
        self.chiefs = ["Шеф_Антон", "Шеф_Сергей", "Шеф_Георгий"]
        self.dish = ["Борщ", "Салат Цезарь", "Стейк", "Паста Карбонара", "Тирамису"]
        self.order_queue = Queue()
        self.condition = Condition()
        self.executor = ThreadPoolExecutor(
            max_workers=len(self.chiefs) + len(self.waiters)
        )
        self.cook_time = random.randint(1, 3)
        self.all_orders_placed = False

    def waiter(self, waiter_name):
        for i in range(3):
            dish = random.choice(self.dish)

            with self.condition:
                self.order_queue.put(dish)
                print(f"{waiter_name} передал заказ на {dish}")

                self.condition.notify()

        with self.condition:
            self.condition.notify()

    def chef(self, chief_name):
        while True:
            with self.condition:
                while self.order_queue.empty() and not self.all_orders_placed:
                    self.condition.wait()

                if self.order_queue.empty() and self.all_orders_placed:
                    break

                dish = self.order_queue.get()
                print(f"{chief_name} готовит {dish}...")

            time.sleep(self.cook_time)
            print(f"{chief_name} закончил готовить {dish}")

    def run(self):
        with self.executor as executor:
            waiter_futures = executor.map(self.waiter, self.waiters)

            with self.condition:
                self.all_orders_placed = True
                self.condition.notify_all()

            chef_futures = executor.map(self.chef, self.chiefs)


service = RestaurantService()
service.run()
