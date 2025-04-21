# Ваша задача вычислить квадраты чисел заданной последовательности в пуле потоков. Для отправки целевой функции в пул потоков используйте метод map().
#
# Выведите результаты вычислений в консоль.
#
# Используйте следующую последовательность чисел: [2, 17, 8, 11, 14, 5].
#
# Результат каждого вычисления должен быть выведен в отдельной строке:

from concurrent.futures import ThreadPoolExecutor


class WorkerSquare:
    def __init__(self, numbers: list):
        self.numbers = numbers
        self.executor = ThreadPoolExecutor(max_workers=5)

    @staticmethod
    def square(n: int):
        return n * n

    def calculate(self):
        with self.executor as executor:
            results = executor.map(self.square, self.numbers)

        [print(result) for result in results]


def main():
    numbers = [2, 17, 8, 11, 14, 5]

    worker = WorkerSquare(numbers)
    worker.calculate()


main()
