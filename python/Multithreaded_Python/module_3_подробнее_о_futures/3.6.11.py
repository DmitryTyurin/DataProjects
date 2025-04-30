# Описание задачи:
# Напишите код для многопоточной обработки заказов на процессоры. Каждый поток будет обрабатывать информацию о наличии и количестве процессоров на складе. В зависимости от результата проверки наличия, функция обратного вызова должна либо подтверждать отправку товара и уменьшать его количество на складе, либо сообщать о невозможности обработки заказа из-за отсутствия товара на складе.
#
# Ваш словарь inventory содержит различные модели процессоров в качестве ключей и их количество на складе в качестве значений.
#
# # Словарь вшит в задачу, вставлять его в поле ответа не нужно
#
# inventory = {
#             'Intel Core i9': 120,
#             'Intel Core i7': 66,
#             'Intel Core i5': 60,
#             'Intel Core i3': 1,
#             'Intel Xeon': 81,
#             'AMD Ryzen 9': 56,
#             'AMD Ryzen 7': 55,
#             'AMD Ryzen 5': 0,
#             'AMD Ryzen 3': 1,
#             'AMD Threadripper': 41,
#             'AMD Epyc': 3,
#             'Intel Pentium': 19,
#             'Intel Celeron': 2,
#             'Qualcomm Snapdragon 888': 54,
#             'Apple M1': 14,
#             'Apple A14 Bionic': 20,
#             'ARM Cortex-A78': 0,
#             'ARM Cortex-A55': 87,
#             'ARM Cortex-M4': 30,
#             'NVIDIA Tegra X1': 2,
#             'Samsung Exynos 2100': 22,
#             'MediaTek Dimensity 1000': 0,
#             'Intel Atom': 0, 'AMD Athlon': 95,
#             'AMD Sempron': 30,
#             'Intel Core 2 Duo': 2,
#             'Intel Core 2 Quad': 1,
#             'Intel Itanium': 2,
#             'AMD Duron': 98, 'AMD FX': 0
# }
# Этот словарь используется для имитации реальной ситуации управления запасами, где программе необходимо обрабатывать и обновлять информацию о количестве товаров в зависимости от поступающих заказов.
#
#
#
# Для каждой задачи и обработки элемента словаря используйте метод add_done_callback() для привязки функции обратного вызова, которая будет проверять и обновлять инвентарь и выводить необходимые сообщения.
#
# Товара ARM Cortex-A78 нет в наличии, обработка невозможна.
# print(f"Товара {item_id} нет в наличии, обработка невозможна.")
#
# # или
#
# Товар отправлен получателю AMD Athlon. Осталось 94
# print(f"Товар отправлен получателю {item_id}. Осталось {remaining}")
#
#
# Обработка каждого элемента словаря:
#
# Каждый элемент словаря представляет собой отдельный заказ. Код должен обработать каждый заказ и вывести соответствующее сообщение с учетом того, что каждый заказ обрабатывает 1 единицу товара.(т.е. Необходимо сформировать по ОДНОМУ заказу с ОДНОЙ  единицей товара для каждой позиции на складе)
#
# Поиск товара Intel Core i9. Количество на складе: 120 шт
#
# print(f"Поиск товара {item_id}. Количество на складе: {inventory[item_id]} шт")
#
#
# Условия для вывода сообщений:
#
# Если товара достаточно на складе, выводится сообщение о том, что товар отправлен получателю и указывается оставшееся количество, см. выше.
# Если товара нет в наличии, выводится сообщение о невозможности обработки заказа, см. выше.

from concurrent.futures import ThreadPoolExecutor
import threading
import time

inventory = {
    "Intel Core i9": 120,
    "Intel Core i7": 66,
    "Intel Core i5": 60,
    "Intel Core i3": 1,
    "Intel Xeon": 81,
    "AMD Ryzen 9": 56,
    "AMD Ryzen 7": 55,
    "AMD Ryzen 5": 0,
    "AMD Ryzen 3": 1,
    "AMD Threadripper": 41,
    "AMD Epyc": 3,
    "Intel Pentium": 19,
    "Intel Celeron": 2,
    "Qualcomm Snapdragon 888": 54,
    "Apple M1": 14,
    "Apple A14 Bionic": 20,
    "ARM Cortex-A78": 0,
    "ARM Cortex-A55": 87,
    "ARM Cortex-M4": 30,
    "NVIDIA Tegra X1": 2,
    "Samsung Exynos 2100": 22,
    "MediaTek Dimensity 1000": 0,
    "Intel Atom": 0,
    "AMD Athlon": 95,
    "AMD Sempron": 30,
    "Intel Core 2 Duo": 2,
    "Intel Core 2 Quad": 1,
    "Intel Itanium": 2,
    "AMD Duron": 98,
    "AMD FX": 0,
}


class DataInventory:
    def __init__(self, inventory: dict):
        self.inventory = inventory
        self.item = 1
        self.lock = threading.Lock()
        self.execute = ThreadPoolExecutor(max_workers=len(self.inventory))

    @staticmethod
    def process_item(item_name: str):
        remaining = inventory.get(item_name)

        print(f"Поиск товара {item_name}. Количество на складе: {remaining } шт")
        return item_name, remaining

    def check_inventory(self, future):
        item_name, remaining = future.result()

        with self.lock:
            if remaining > 0:
                remaining -= 1
                print(f"Товар отправлен получателю {item_name}. Осталось {remaining}")
            else:
                print(f"Товара {item_name} нет в наличии, обработка невозможна.")

    def run(self):
        with self.execute as executor:
            futures = [
                executor.submit(self.process_item, item_name)
                for item_name in self.inventory
            ]

            for future in futures:
                future.add_done_callback(self.check_inventory)


di = DataInventory(inventory)
di.run()
