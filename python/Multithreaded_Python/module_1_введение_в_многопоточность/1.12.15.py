# Напишите программу, которая будет использовать несколько потоков для выполнения целевой функции. А по истечении заданного времени будет выводить список активных потоков.
#
# Ключевые моменты:
#
# Напишите целевую функцию, принимающую в качестве аргумента время, которое будет имитировать длительность работы. Функция должна выводить:
# Поток <имя потока> начал работу
# затем имитировать работу и после чего выводить:
# Поток <имя потока> завершил работу
# В качестве имени функции используйте my_task
# Запустите необходимое количество потоков. Для передачи аргументов целевой функции используйте вшитый в тестирующую систему список delays
# По истечении 1.5 секунд выведите в консоль активные потоки, в виде:
# <имя потока> еще выполняется

import threading
import time

delays = [0.7, 2.4, 1, 8, 4.3, 0.4, 1.3, 2.5, 1.7, 3.2, 4.7, 3.6]


class ThreadTracker:
    def __init__(self, delays: list):
        self.delays = delays
        self.threads = []

    @staticmethod
    def my_task(delay: float):
        current_thread = threading.current_thread()

        print(f"Поток {current_thread.name} начал работу")
        time.sleep(delay)
        print(f"Поток {current_thread.name} завершил работу")

    def create_threads(self):
        self.threads = [
            threading.Thread(target=self.my_task, args=(delay,))
            for i, delay in enumerate(self.delays)
        ]

    def run_threads(self):
        self.create_threads()

        [thread.start() for thread in self.threads]

    @staticmethod
    def print_active_threads():
        active_threads = threading.enumerate()
        [print(f"{thread.name} еще выполняется") for thread in active_threads]

    def join_threads(self):
        [thread.join() for thread in self.threads]


def main():
    tracker = ThreadTracker(delays)

    tracker.run_threads()

    time.sleep(1.5)
    tracker.print_active_threads()

    tracker.join_threads()


main()
