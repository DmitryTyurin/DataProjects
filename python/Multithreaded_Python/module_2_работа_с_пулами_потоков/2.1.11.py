# Описание задачи:
# Напишите код, использующий ThreadPoolExecutor для параллельного выполнения трех различных математических задач. Ваша программа должна включать следующие функции:
#
# Вычисление числа Фибоначчи: Напишите функцию fib_future(), которая рекурсивно вычисляет n-е число Фибоначчи. Используйте пул потоков для вычисления, например, 20-го числа Фибоначчи.
#
# Сумма квадратных корней: Создайте функцию для вычисления суммы квадратных корней чисел в заданном диапазоне
#
# sqrt_future(). Используйте пул потоков для одновременного вычисления суммы квадратных корней чисел от 1 до 50(включительно).
#
# Вычисление факториала числа: Реализуйте функцию, которая вычисляет факториал заданного числа
#
# fact_result(). Используйте пул потоков для вычисления, например, факториала числа 20.
#
# Вывод результата: Для получения необходимого результата, используйте следующие принты.
#
# print(f"20-е число Фибоначчи: {fib_result}")
# print(f"Сумма квадратных корней чисел от 1 до 50: {sqrt_result:.4f}")
# print(f"Факториал числа 20: {fact_result}")

from concurrent.futures import ThreadPoolExecutor
import math

PARAMS = [20, 1, 50, 20]


class MathTasks:
    def __init__(self, params: list[int]) -> None:
        self.params = params
        self.fibonacci_number = self.params[0]
        self.sum_start_number = self.params[1]
        self.sum_end_number = self.params[2]
        self.factorial_number = self.params[3]

    def fibonacci(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def sum_of_square_roots(self, start: int, end: int) -> float | int:
        return sum(math.sqrt(i) for i in range(start, end + 1))

    def factorial(self, n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)

    def calculate_tasks(self):
        with ThreadPoolExecutor() as executor:
            fib_future = executor.submit(self.fibonacci, self.fibonacci_number)
            sqrt_future = executor.submit(
                self.sum_of_square_roots, self.sum_start_number, self.sum_end_number
            )
            fact_future = executor.submit(self.factorial, self.factorial_number)

            fib_result = fib_future.result()
            sqrt_result = sqrt_future.result()
            fact_result = fact_future.result()

        print(f"{self.fibonacci_number}-е число Фибоначчи: {fib_result}")
        print(
            f"Сумма квадратных корней чисел от {self.sum_start_number} до {self.sum_end_number}: {sqrt_result:.4f}"
        )
        print(f"Факториал числа {self.factorial_number}: {fact_result}")


def main():
    math_tasks = MathTasks(PARAMS)
    math_tasks.calculate_tasks()


main()
