# Напишите программу, которая будет вычислять факториал заданных чисел и возвращать результат, по мере готовности.
#
# Ключевые моменты:
#
# Напишите функцию для вычисления факториала, передаваемого числа. Для имитации длительности работы используйте задержку в размере 1/10 от передаваемого в функцию числа.
# Для конкуретного выполнения задач используйте пул потоков. Выведите в консоль результаты по мере их готовности, в виде:
#           Факториал числа <число> равен <результат>


from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
import time
import math

numbers = [5, 4, 7, 6, 3]


class DataFactorial:
    def __init__(self, numbers: list):
        self.numbers = numbers

    @staticmethod
    def calculate(num: int) -> tuple:
        time.sleep(num / 10)

        return num, math.factorial(num)

    def run(self):
        with ThreadPoolExecutor(max_workers=len(self.numbers)) as executor:
            futures = {executor.submit(self.calculate, num) for num in self.numbers}

            done, pending = wait(futures, return_when=ALL_COMPLETED)

            [
                print(f"Факториал числа {task.result()[0]} равен {task.result()[1]}")
                for task in done
            ]


def main():
    data_factorial = DataFactorial(numbers=numbers)
    data_factorial.run()


main()
