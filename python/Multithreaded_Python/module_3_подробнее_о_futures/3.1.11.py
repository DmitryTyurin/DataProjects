# Описание задачи: Напишите программу, которая использует ThreadPoolExecutor для обработки чисел с учетом времени их выполнения. В программе заданы два списка: список timeouts = [...] и список чисел numbers = [...]. Ключевой особенностью является то, что порядковые номера элементов в обоих списках сопоставимы и должны быть обработаны одновременно. Т.е. для числа 2257 timeout=4, а для числа 6217 timeout=5 (согласно спискам ниже) и т.д.
#
# Количество элементов в списках идентичное.
#
# timeouts = [4, 5, 3, 5, 4, 2, 5, 1, 3, 5, 3, 5, 1, 5, 5, 2, 1, 5, 1, 2]
# numbers = [2257, 6217, 6594, 2259, 5284, 3568, 1741, 5462, 7494, 8971, 3157, 3998, 2040, 8828, 8769, 6976, 9367, 1267, 6255, 7322]
# Функция process_number(timeout, number) имитирует длительную задачу, ожидая заданное количество времени, прежде чем возвращать число.
#
# def process_number(timeout, number):
#     time.sleep(timeout)
#     return number
# С помощью ThreadPoolExecutor, программа должна создать множество потоков для параллельной обработки чисел с их соответствующими временами ожидания.
# Основная цель - собрать и суммировать те числа, время обработки которых не превышает 3 секунды. Программа должна игнорировать числа, обработка которых занимает больше чем 3 секунды. (По факту, вам может потребоваться немного больше времени на обработку задач, т.к. затрачивается время на создание пула, и переключение между потоками, это может привести к несущественным задержкам например: 3.0028076171875 секунды)

from concurrent.futures import ThreadPoolExecutor, wait
import time

timeouts = [4, 5, 3, 5, 4, 2, 5, 1, 3, 5, 3, 5, 1, 5, 5, 2, 1, 5, 1, 2]
numbers = [
    2257,
    6217,
    6594,
    2259,
    5284,
    3568,
    1741,
    5462,
    7494,
    8971,
    3157,
    3998,
    2040,
    8828,
    8769,
    6976,
    9367,
    1267,
    6255,
    7322,
]


class GetSumNumbers:
    def __init__(self, timeout: list, numbers: list):
        self.timeouts = timeout
        self.numbers = numbers
        self.item_zip = zip(self.timeouts, self.numbers)
        self.executor = ThreadPoolExecutor()
        self.result = []

    @staticmethod
    def process_number(timeout: int, number: int):
        if timeout > 3:
            return 0

        time.sleep(timeout)
        return number

    def process_summary_numbers(self):
        with self.executor as executor:
            futures = [
                executor.submit(self.process_number, timeout, number)
                for timeout, number in self.item_zip
            ]

            for future in futures:
                self.result.append(future.result())

    def get_summary_numbers(self):
        if self.result:
            return sum(self.result)
        else:
            return 0


def main():
    sum_numbers = GetSumNumbers(timeouts, numbers)
    sum_numbers.process_summary_numbers()
    print(sum_numbers.get_summary_numbers())


main()
