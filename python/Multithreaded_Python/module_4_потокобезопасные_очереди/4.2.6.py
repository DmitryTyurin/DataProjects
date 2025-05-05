# Необходимо написать программу, в которой с помощью потокобезопасной очереди будут обрабатываться 10 элементов в определенном порядке.
#
# Для этого напишите 2 целевые функции:
#
# Для добавления в очередь элементов. Функция должна имитировать задержку в 0.5 секунды после каждого добавления. Также при добавлении элемента нужно выводить в консоль: Добавлен: <элемент>, а после добавления всех элементов: Все элементы добавлены
# Для извлечения из очереди элементов. Функция должна имитировать ожидание  каждого элемента  1 секунду, а после извлечения будет выводить в консоль: Извлечен: <элемент>
# После обработки очереди выведите в консоль: Все элементы очереди обработаны

import threading
import queue
import time


elements = [
    "телевизор",
    "холодильник",
    "микроволновка",
    "утюг",
    "чайник",
    "пылесос",
    "стиральная машина",
    "кофеварка",
    "фен",
    "утюг",
]


class DataPutFromQueue:
    def __init__(self, elements: list):
        self.queue = queue.Queue()
        self.timeout = 1
        self.elements = elements

    def producer(self):
        for element in self.elements:
            time.sleep(0.5)

            self.queue.put(element)
            print(f"Добавлен: {element}")

        print("Все элементы добавлены")

    def consumer(self):
        while True:
            try:
                item = self.queue.get(timeout=self.timeout)
                print(f"Извлечен: {item}")
            except queue.Empty:
                print("Все элементы очереди обработаны")
                break

    def run_threads(self):
        producer = threading.Thread(target=self.producer)
        consumer = threading.Thread(target=self.consumer)

        producer.start()
        consumer.start()

        producer.join()
        consumer.join()


dpq = DataPutFromQueue(elements)
dpq.run_threads()
