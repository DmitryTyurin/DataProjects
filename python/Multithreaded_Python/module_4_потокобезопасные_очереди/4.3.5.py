# Ваша задача написать программу, которая будет в многопоточном режиме обрабатывать элементы стека.
#
# Ключевые этапы:
#
# Напишите функцию, которая будет извлекать из очереди элементы в обратном порядке добавления. Во время извлечения будет выводить в консоль: Обработка элемента: <элемент>
# Создайте стек. Для добавления в него элементов используйте следующие данные:
#           data = [15, 13, 7, 19, 3, 1, 11, 5, 9, 17]
#
# Создайте и запустите 3 потока, для обработки стека.
# После обработки всех элементов очереди выведите в консоль: Все элементы успешно обработаны

from concurrent.futures import ThreadPoolExecutor, wait
import queue
import time


data = [15, 13, 7, 19, 3, 1, 11, 5, 9, 17]


class DataPutFromQueue:
    def __init__(self, elements: list):
        self.elements = elements
        self.stack = queue.LifoQueue()
        self.data_stack = [self.stack.put(element) for element in elements]
        self.executor = ThreadPoolExecutor(max_workers=4)

    def process_stack(self):
        while self.stack.qsize() > 0:
            print(f"Обработка элемента: {self.stack.get()}")

            self.stack.task_done()
            time.sleep(0.1)

    def run(self):
        with self.executor as executor:
            futures = [executor.submit(self.process_stack)]

            wait(futures, return_when="ALL_COMPLETED")

        self.stack.join()

        print("Все элементы успешно обработаны")


dpq = DataPutFromQueue(data)
dpq.run()
