# Напишите программу, которая будет вычислять квадрат передаваемого числа или его факториал, в зависимости от его величины.
#
# Ключевые моменты:
#
# Определите функцию для обработки числа. Если число меньше или равно семи, то необходимо вычислить его факториал, если больше - его квадрат. Функция должна сообщать о начале обработки числа, в виде:
#           Обработка числа <число> началась
#
#           затем должна имитировать время работы, в виде задержки в 1/10 секунды от передаваемого числа и в заключении
#           возвращать необходимый результат вычислений;
#
# Используйте ручное управление пулом потоков;
# По завершению вычислений выведите в консоль сумму полученных результатов в виде:
#           Сумма обработанных чисел равна <результат>
#
#
#
# Используйте следующую последовательность чисел: [19, 1, 4, 13, 10, 7, 16]

from concurrent.futures import ThreadPoolExecutor
import time
import math

numbers = [19, 1, 4, 13, 10, 7, 16]


class FactorialSquare:
    def __init__(self, numbers: list):
        self.number = numbers
        self.executor = ThreadPoolExecutor()

    @staticmethod
    def worker(number: int):
        print(f"Обработка числа {number} началась")
        time.sleep(0.1)

        if number <= 7:
            result = math.factorial(number)
        else:
            result = number**2

        return result

    def run(self):
        with self.executor as executor:
            futures = executor.map(self.worker, self.number)
            executor.shutdown(wait=True)

        total = sum(futures)
        print(f"Сумма обработанных чисел равна {total}")


FactorialSquare(numbers).run()
