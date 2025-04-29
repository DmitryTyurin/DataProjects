# Описание задачи:
# Используйте многопоточность обработки трёх различных списков, каждый из которых содержит числовые значения.
#
# # Списки чисел для обработки вшиты в задачу, их можно не вставлять в поле ответа.
# small_numbers = list(range(1, 51))
# medium_numbers = list(range(51, 151))
# large_numbers = list(range(151, 301))
# Ваша задача - создать пары «ключ-значение», где ключом является элемент из списка, а значением - результат выполнения некоторой функции с этим элементом. Размер пула потоков для каждого списка будет различаться, что позволит исследовать эффективность многопоточной обработки при разных условиях.
#
# Списки и функции:
#
# Список small_numbers - содержит числа от 1 до 50. Функция для обработки - возведение числа в квадрат.
# Список medium_numbers - содержит числа от 51 до 150. Функция для обработки - вычисление куба числа.
# Список large_numbers - содержит числа от 151 до 300. Функция для обработки - нахождение факториала числа.
# Программа должна включать функцию process_number, которая принимает число и функцию обработки, возвращая пару «ключ-значение», где ключ - это исходное число, а значение - результат выполнения функции.
#
# # Функция для обработки числа с использованием заданной функции
# def process_number(number, function):
#     return {number: function(number)}
#
# Основная функция main() будет использоваться для создания пула потоков и параллельной обработки элементов каждого списка.
#
# Требования к выводу: Программа должна обрабатывать каждый список (small_numbers, medium_numbers, large_numbers) с соответствующим размером пула потоков (например, 10, 20, 30). Вывод должен отображать сгенерированные пары «ключ-значение» для каждого списка.

from concurrent.futures import ThreadPoolExecutor, as_completed
import math
from functools import partial


class NumberProcessor:
    def __init__(self):
        self.small_numbers = list(range(1, 51))
        self.medium_numbers = list(range(51, 151))
        self.large_numbers = list(range(151, 301))

    @staticmethod
    def square(number):
        return number**2

    @staticmethod
    def cube(number):
        return number**3

    @staticmethod
    def factorial(number):
        return math.factorial(number)

    @staticmethod
    def process_number(number, function):
        return {number: function(number)}

    def process_list(self, numbers, function, pool_size):
        results = []
        with ThreadPoolExecutor(max_workers=pool_size) as executor:
            process_func = partial(self.process_number, function=function)

            futures = [executor.submit(process_func, num) for num in numbers]

            for future in as_completed(futures):
                results.append(future.result())

        return results

    def run(self):
        results_small = self.process_list(self.small_numbers, self.square, 10)
        results_medium = self.process_list(self.medium_numbers, self.cube, 20)
        results_large = self.process_list(self.large_numbers, self.factorial, 30)

        print("Результаты для маленьких чисел (возведение в квадрат):")
        for result in results_small:
            print(result)

        print("\nРезультаты для средних чисел (возведение в куб):")
        for result in results_medium:
            print(result)

        print("\nРезультаты для больших чисел (факториал):")
        for result in results_large:
            print(result)


processor = NumberProcessor()
processor.run()
