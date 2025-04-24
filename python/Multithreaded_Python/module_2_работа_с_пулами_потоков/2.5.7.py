# Описание задачи:
#
# Ваша задача - написать многопоточный код для сортировки массива из 150 случайно сгенерированных чисел от 1 до 999 и последующего их распределения по четырем диапазонам:
#
# от 1 до 300,
# от 301 до 500
# от 501 до 700
# от 701 до 999
# Каждый диапазон должен быть обработан в отдельном потоке.
#
#
# Вам дан список numbers=[] , содержащий 150 случайных чисел, каждое из которых лежит в диапазоне от 1 до 999. Используя многопоточность, вам нужно отсортировать эти числа и разделить их на четыре категории по диапазонам. Это позволит быстрее и эффективнее работать с числами в будущем, обеспечивая легкий доступ к необходимым данным.
#
# Шаги выполнения задачи:
#
# Отсортируйте список numbers=[], чтобы числа шли в порядке возрастания(список numbers=[] вшит в задачу).
#
# Разделите отсортированные числа на четыре группы в зависимости от их значений. Эти группы соответствуют диапазонам от 1 до 300, от 301 до 500, от 501 до 700 и от 701 до 999.
#
# Для каждого диапазона чисел выведите соответствующие сообщения с перечислением всех чисел, попадающих в данный диапазон. Вывод должен быть примерно следующий
#
# Числа в массиве от 1 до 300 [11, 25, 29, 45, 48, 50, ...]
# Числа в массиве от 301 до 500 [305, 306, 310, 316, 317, ...]
# Числа в массиве от 501 до 700 [503, 517, 522, 526, 542, 548, ...]
# Числа в массиве от 701 до 999 [706, 719, 729, 738, 745, 751, 752, ...]
#
#
# Числа в массиве от 1 до 300

from concurrent.futures import ThreadPoolExecutor
from random import randint

numbers = [randint(1, 999) for _ in range(150)]
sorted_numbers = sorted(numbers)
ranges = [(1, 300), (301, 500), (501, 700), (701, 999)]


class NumberSorter:
    def __init__(self, numbers: list[int], start: int, end: int):
        self.numbers = numbers
        self.start = start
        self.end = end

    def process(self):
        return [num for num in self.numbers if self.start <= num <= self.end]

    def print_result(self):
        result = self.process()
        print(f"Числа в массиве от {self.start} до {self.end} {result}")


def main():
    with ThreadPoolExecutor(max_workers=4) as executor:
        filters = [NumberSorter(sorted_numbers, start, end) for start, end in ranges]
        futures = {executor.submit(filter.print_result): filter for filter in filters}

    [future.result() for future in futures]


main()
