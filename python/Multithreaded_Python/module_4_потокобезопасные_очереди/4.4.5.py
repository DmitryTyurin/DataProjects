# Создайте многопоточное приложение, которое будет добавлять в очередь и извлекать из нее элементы, согласно их приоритетам.
#
# Ключевые моменты:
#
# Создайте приоритетную очередь размерностью в 5 элементов;
# Напишите функцию, которая будет извлекать элементы из очереди с имитацией времени выполнения, исходя из величины priority (приоритета):
# time.sleep(priority/100)
# По результату извлечения она должна выводить в консоль:
# Обработан "<элемент>"
# Напишите функцию для добавления в очередь элементов;
# Создайте и запустите 2 потока с целевыми функциями-потребителями;
# Создайте и запустите отдельный поток с функцией-производителем.

import queue
import threading
import time
from concurrent.futures import ThreadPoolExecutor, wait

electronics = [
    (1, "смартфон"),
    (15, "ноутбук"),
    (7, "планшет"),
    (33, "камера"),
    (67, "гарнитура"),
    (4, "телевизор"),
    (21, "гаджет"),
    (83, "монитор"),
    (0, "роутер"),
    (47, "плеер"),
]


class PriorityProcessor:
    def __init__(self, elements: list):
        self.elements = elements
        self.priority_queue = queue.PriorityQueue(maxsize=5)
        self.lock = threading.Lock()
        self.executor = ThreadPoolExecutor(max_workers=3)

    def producer(self):
        for i in electronics:
            self.priority_queue.put(i)

    def process_stack(self):
        while self.priority_queue.qsize() > 0:
            priority, item = self.priority_queue.get()
            time.sleep(priority / 100)

            with self.lock:
                print(f'Обработан "{item}"')

            self.priority_queue.task_done()

    def run(self):
        with self.executor as executor:
            futures = [
                executor.submit(
                    self.producer,
                ),
                executor.submit(self.process_stack),
                executor.submit(self.process_stack),
            ]


processor = PriorityProcessor(electronics)
processor.run()
