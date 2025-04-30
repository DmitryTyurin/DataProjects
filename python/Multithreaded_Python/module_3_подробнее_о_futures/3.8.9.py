# Напишите программу, которая отменяет заданное количество задач, отправленных в пул потоков. А для выполнившихся задач — выводит их результаты.
#
# Ключевые моменты:
#
# Напишите функцию, которая в качестве аргумента принимает кортеж из двух элементов: название задачи и длительность ее выполнения. По итогу своего "выполнения" возвращает:
# Задача <название задачи> выполнилась за <длительность выполнения> секунды
# Для отправки задач с аргументами используйте список data, который вшит в тестирующую систему.
# data = []
# Следует выполнить только 5 первых задач из 10 (длина data равна 10), а остальные - отменить.


from concurrent.futures import ThreadPoolExecutor
import time

data = [
    ("CPU", 3.1),
    ("RAM", 1.5),
    ("GPU", 1.6),
    ("Motherboard", 1.8),
    ("SSD", 1.3),
    ("Keyboard", 1.5),
    ("Mouse", 3.9),
    ("Monitor", 2.8),
    ("Headphones", 3.0),
    ("Router", 1.0),
]


class TaskProcessor:
    def __init__(self, data: list):
        self.data = data
        self.executor = ThreadPoolExecutor(max_workers=5)

    @staticmethod
    def process(task_info: tuple):
        task_name, duration = task_info

        time.sleep(duration / 10)

        return f"Задача {task_name} выполнилась за {duration} секунды"

    def run(self):
        with self.executor as executor:
            futures = [
                executor.submit(self.process, task_info) for task_info in self.data
            ]

            for future in futures[5:]:
                future.cancel()

            for future in futures[:5]:
                if not future.cancelled():
                    print(future.result())


tp = TaskProcessor(data)
tp.run()
