# Расчет факториала числа с использованием пула потоков и функции apply()
# Используйте метод apply(), чтобы рассчитать факториал числа в многопоточной среде.
#
# Функция factorial(n): Принимает целое число и возвращает его факториал.
# Функция calculate_factorial(numbers): Принимает список чисел и использует пул потоков для параллельного расчета факториалов этих чисел. Создайте пул потоков с помощью ThreadPool(4), означающий, что вы хотите использовать 4 потока для выполнения задач. Для каждого числа в списке numbers используйте метод pool.apply(), чтобы выполнить функцию factorial для данного числа. Метод apply() блокирует выполнение до тех пор, пока задача не будет завершена, и возвращает результат выполнения функции. После выполнения всех задач не забудьте закрыть пул и дождаться завершения всех потоков с помощью методов pool.close() и pool.join().
#
#
# Цель этой задачи - научиться использовать метод apply() для выполнения синхронных задач в пуле потоков. Этот метод позволяет выполнять функции в отдельных потоках, блокируя выполнение до получения результата. Это полезно в ситуациях, когда необходимо дождаться завершения задачи перед продолжением выполнения программы. Особое внимание уделите тому, как аргументы передаются в функцию: используйте кортежи для передачи аргументов в функцию factorial, которая будет выполняться в потоках пула.
#
# Sample Input:
#
# 5
# 3
# 7
# 11
# 17
# 23
# 25
# 29
# 30
# Sample Output:
#
# 120
# 6
# 5040
# 39916800
# 355687428096000
# 25852016738884976640000
# 15511210043330985984000000
# 8841761993739701954543616000000
# 265252859812191058636308480000000

from multiprocessing.pool import ThreadPool

numbers = [5, 3, 7, 11, 17, 23, 25, 29, 30]


class FactorialMultiplier:
    def __init__(self, number_list: list[int]):
        self.number_list = number_list
        self.results = []
        self.pool = ThreadPool(processes=4)

    def factorial(self, number):
        if number == 0:
            return 1
        else:
            return number * self.factorial(number - 1)

    def calculate_factorial(self):
        with self.pool as pool:
            for number in self.number_list:
                if number > 0:
                    result = pool.apply(self.factorial, (number,))
                    self.results.append(result)

        return self.results


factorial_multi = FactorialMultiplier(numbers)
results = factorial_multi.calculate_factorial()

[print(i) for i in results]
