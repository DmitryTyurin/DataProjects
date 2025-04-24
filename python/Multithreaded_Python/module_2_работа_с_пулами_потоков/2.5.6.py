# Описание задачи:
#
#  Ваша задача - разработать функцию для вычисления степеней чисел и запустить ее в пул потоков.
#
# Вам даны два списка: один содержит основания (bases), а другой - показатели степеней (exponents). Необходимо написать код, который возведет каждое основание в соответствующую степень, используя многопоточность, чтобы обработать все вычисления одновременно.
#
# Шаги выполнения задачи:
#
# У вас есть два списка: bases = [] и exponents = []. Каждый элемент списка bases должен быть возведен в степень элемента из списка exponents, находящегося на той же позиции.
# # Полные списки вшиты в задачу
#
# bases = [3, 44, 22, ...,]
# exponents = [12, 31, ...,]
# Создайте функцию power(base, exponent), которая принимает основание и показатель степени, возвращая результат возведения в степень. Для каждой успешно вычисленной степени выводите результат в консоль, используя форматирование строк, чтобы показать, какое основание было возведено в какую степень и какой получился результат.
# 3 в степени 12 равно 531441
#
# print(f"{base} в степени {exponent} равно {result}")
# Используйте ThreadPoolExecutor  для создания пула потоков. Примените метод map для добавления задач в пул потоков.

from concurrent.futures import ThreadPoolExecutor

bases = [
    3,
    44,
    22,
]
exponents = [12, 31, 27]


class PowerCalculator:
    def __init__(self):
        pass

    @staticmethod
    def power(base: int | float, exponent: int | float) -> None:
        result = base**exponent
        print(f"{base} в степени {exponent} равно {result}")

    def run(self, bases: list[int | float], exponents: list[int | float]) -> None:
        with ThreadPoolExecutor() as executor:
            executor.map(self.power, bases, exponents)


def main():
    calculator = PowerCalculator()
    calculator.run(bases, exponents)


main()
