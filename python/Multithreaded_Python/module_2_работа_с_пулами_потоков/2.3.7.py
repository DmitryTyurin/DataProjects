# Измените решение этой задачи, используя пул потоков.
# Для создания пула потоков и отправки в него целевых функций с помощью метода submit() напишите функцию main().

from concurrent.futures import ThreadPoolExecutor


class PrintData:
    def __init__(self):
        pass

    @staticmethod
    def print_numbers():
        [print(i) for i in range(1, 6)]

    @staticmethod
    def print_letters():
        [print(chr(i)) for i in range(97, 102)]

    def create_pool(self):
        with ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(self.print_numbers)
            executor.submit(self.print_letters)


def main():
    print_data = PrintData()
    print_data.create_pool()

    print("Готово!")


main()
