# Цель задачи:
# Создать 10 потоков для выполнения 10 задач, каждому потоку присваивается уникальный ID. Эти ID используются для инициализации каждого потока, и все потоки работают конкурентно.

from concurrent.futures import ThreadPoolExecutor, wait
from threading import current_thread
import time
from queue import Queue


class WorkerQueue:
    def __init__(self):
        self.queue = Queue()
        self.thread_id_generator = self.get_unique_thread_id()
        self.executor = ThreadPoolExecutor(
            max_workers=10, initializer=self.thread_initializer
        )

    @staticmethod
    def get_unique_thread_id():
        unique_thread_ids = [
            "KFD34",
            "DGS6D",
            "F7F9S",
            "SDG0D",
            "WQ9WE",
            "29AXC",
            "AF632",
            "DCV13",
            "Q9ETF",
            "1D0S3",
        ]

        for thread_id in unique_thread_ids:
            yield thread_id

    def thread_initializer(self):
        thread_id = next(self.thread_id_generator)

        self.queue.put(f"Инициализация потока: {thread_id}")

        current_thread().thread_id = thread_id

    def thread_task(self, task_num: int):
        thread_id = current_thread().thread_id

        self.queue.put(f"Задача {task_num} запущена")
        time.sleep(1)
        self.queue.put(f"Задача {task_num} выполнена")

    def print_results(self):
        while not self.queue.empty():
            print(self.queue.get())

    def run(self):
        with self.executor as executor:
            futures = {executor.submit(self.thread_task, i) for i in range(10)}

            wait(futures)

        self.print_results()


WorkerQueue().run()
