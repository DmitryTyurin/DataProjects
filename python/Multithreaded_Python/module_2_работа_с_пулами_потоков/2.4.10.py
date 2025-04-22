# Напишите программу, которая будет получать результаты выполненных задач через заданное время.
#
# Ключевые моменты:
#
# Напишите простую функцию, которая принимает 2 аргумента: имя и время выполнения задачи. Функция должна имитировать работу в течение переданного ей времени работы и возвращать ее имя.
# Используйте пул потоков. Получите и выведите результаты тех задач, время выполнения которых длится менее 1.5 секунд.
#
#
# Для передачи аргументов целевым функциям предлагается использовать следующий список:
#
# data = [("asdf", 0.7), ("ghjk", 1.4), ("zxcl", 3.2), ("vbnm", 4.1), ("poiu", 2.7), ("ytre", 0.3), ("wqsx", 1.1)]
# Вставьте этот список в решение.

from concurrent.futures import ThreadPoolExecutor, as_completed
import time


class TaskCompleted:
    def __init__(self, data: list):
        self.data = data

    @staticmethod
    def print_task_name(name: str, duration: float | int) -> str:
        time.sleep(duration)

        return name

    def run_tasks(self) -> None:
        with ThreadPoolExecutor() as executor:
            try:
                futures = {
                    executor.submit(self.print_task_name, name, duration)
                    for name, duration in self.data
                }

                for future in as_completed(futures, timeout=1.5):
                    print(future.result())
            except TimeoutError as te:
                pass


def main():
    data = [
        ("asdf", 0.7),
        ("ghjk", 1.4),
        ("zxcl", 3.2),
        ("vbnm", 4.1),
        ("poiu", 2.7),
        ("ytre", 0.3),
        ("wqsx", 1.1),
    ]
    task_completed = TaskCompleted(data)
    task_completed.run_tasks()


main()
