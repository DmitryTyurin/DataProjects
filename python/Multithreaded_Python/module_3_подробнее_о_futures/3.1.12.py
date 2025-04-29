# Описание задачи: Напишите программу, использующую ThreadPoolExecutor для конкурентного умножения чисел из четырех различных списков и обработки исключений.
#
# # Списки вшиты в задачу, вставлять их в поле ответа не нужно
# list1 = [16,10, ..]
# list2 = [0,7, ..]
# list3 = [8,19, ..]
# list4 = [1,0, ..]
# Вам предоставлены четыре списка. Каждый список содержит набор чисел от 0 до 20, и ваша задача - создать список кортежей, где каждый кортеж содержит по одному числу из каждого списка. Затем, используя многопоточность, вычислите произведение чисел в каждом кортеже.
# Например: если брать числа из списков выше, то необходимо умножить между собой числа  16*0*8*1, затем 10*7*19*0 и так далее.
#
# Каждый список содержит случайный набор чисел. Программа должна брать по порядку по одному числу из каждого списка и умножить их между собой. Используя ThreadPoolExecutor, программа должна параллельно вычислять произведение четырёх чисел. В случае обнаружения числа 0 (что приведет к произведению на ноль), программа должна обрабатывать исключение ValueError и выводить соответствующее сообщение.
#
# Требования к выводу: Программа должна выводить результат умножения чисел д

from concurrent.futures import ThreadPoolExecutor

list1 = [16, 10, 14, 7, 10, 12, 16, 10, 16, 10, 16, 4, 16, 10, 16, 10, 16, 10, 16, 10]
list2 = [0, 7, 5, 11, 0, 8, 4, 14, 8, 14, 8, 17, 8, 14, 8, 14, 8, 14, 8, 14]
list3 = [8, 19, 13, 10, 17, 8, 17, 11, 17, 11, 17, 10, 17, 11, 17, 11, 17, 11, 17, 11]
list4 = [1, 0, 17, 4, 19, 8, 19, 2, 19, 2, 19, 8, 19, 2, 19, 2, 19, 2, 19, 2]


class NumberMultiplier:
    def __init__(self, list1: list, list2: list, list3: list, list4: list):
        self.list1 = list1
        self.list2 = list2
        self.list3 = list3
        self.list4 = list4
        self.all_lists = list(zip(self.list1, self.list2, self.list3, self.list4))
        self.executor = ThreadPoolExecutor(max_workers=4)

    @staticmethod
    def multiply_numbers(a, b, c, d):
        try:
            result = a * b * c * d
            if 0 in (a, b, c, d):
                raise ValueError("Обнаружено умножение на ноль")
            return result
        except ValueError as e:
            raise e

    def process_numbers(self, numbers: list):
        a, b, c, d = numbers

        try:
            result = self.multiply_numbers(a, b, c, d)
            print(f"Результат: {result}")
        except ValueError as e:
            print(f"Обработано исключение: {e}")

    def run(self):
        with self.executor as executor:
            executor.map(self.process_numbers, self.all_lists)


def main():
    number_multiplier = NumberMultiplier(list1, list2, list3, list4)
    number_multiplier.run()


main()
