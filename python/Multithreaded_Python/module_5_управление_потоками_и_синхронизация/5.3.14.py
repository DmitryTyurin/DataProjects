# Ваша задача написать программу, которая будет имитировать обслуживание клиентов в банке несколькими кассирами.
#
# Ключевые моменты:
#
# Для имитации поведения клиента напишите функцию, которая принимает, в качестве аргумента, имя клиента, выводя:
# <имя клиента> вошел в банк
# После обслуживания функция выводит:
# <имя клиента> обслужен и покидает банк
# Для имитации работы кассира напишите функцию, которая принимает, в качестве аргумента, имя клиента, выводя:
# Обслуживаю клиента <имя клиента>
# Обслуживание клиента занимает какое-то время.
# После обслуживания функция выводит:
# Клиент <имя клиента> обслужен
# Организуйте синхронизированное обслуживание клиентов.
# Используйте следующий список клиентов: ["Виктор", "Ирина", "Андрей"]
#
# Убедитесь, что все клиенты обслужены прежде, чем закрыть банк:
#
# Все клиенты обслужены. Банк закрывается.
# Перед тем, как отправить решение в тестирующую систему - проверьте его на своей машине.

from concurrent.futures import ThreadPoolExecutor
import threading
import time
import random

clients = ["Виктор", "Ирина", "Андрей"]


class BankingService:
    def __init__(self, clients: list):
        self.clients = clients
        self.executor = ThreadPoolExecutor(max_workers=3)
        self.lock = threading.Lock()
        self.random_time = random.randint(1, 3)

    def process_bank_management(self, client: str):
        print(f"Обслуживаю клиента {client}")

        time.sleep(self.random_time)

        print(f"Клиент {client} обслужен")

    def process_client(self, client: str):
        with self.lock:
            print(f"{client} вошел в банк")

            self.process_bank_management(client)

            print(f"{client} обслужен и покидает банк")

    def run(self):
        with self.executor as executor:
            futures = [
                executor.submit(self.process_client, client) for client in self.clients
            ]

        if all(future.done() for future in futures):
            print("Все клиенты обслужены. Банк закрывается.")


service = BankingService(clients)
service.run()
