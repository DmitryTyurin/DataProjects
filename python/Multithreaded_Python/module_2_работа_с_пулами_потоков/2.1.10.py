# Описание задачи:
# Допишите код ниже, который будет использовать многопоточность для параллельного вычисления сумм чисел в нескольких диапазонах.
#
# Ваша задача - использовать класс ThreadPoolExecutor для создания пула потоков, который будет одновременно обрабатывать три разных диапазона чисел и функцию sum_range() которая представлена в поле ответа:
#
# от 1 до 100
# от 101 до 200
# и от 201 до 300
# Для каждого диапазона необходимо вычислить сумму чисел и вывести результаты.
#
# print(f"Сумма чисел от 1 до 100: {sum1}")
# print(f"Сумма чисел от 101 до 200: {sum2}")
# print(f"Сумма чисел от 201 до 300: {sum3}")

from concurrent.futures import ThreadPoolExecutor


class RangeSumCalculator:
    def __init__(self):
        self.sum1 = 1
        self.sum2 = 101
        self.sum3 = 201

    @staticmethod
    def sum_range(start):
        return sum(range(start, (start + 100)))

    def calculate_sums(self):
        with ThreadPoolExecutor(max_workers=3) as executor:
            sum1 = executor.submit(self.sum_range, self.sum1)
            sum2 = executor.submit(self.sum_range, self.sum2)
            sum3 = executor.submit(self.sum_range, self.sum3)

            print(f"Сумма чисел от 1 до 100: {sum1.result()}")
            print(f"Сумма чисел от 101 до 200: {sum2.result()}")
            print(f"Сумма чисел от 201 до 300: {sum3.result()}")


def main():
    calculator = RangeSumCalculator()
    calculator.calculate_sums()


main()
