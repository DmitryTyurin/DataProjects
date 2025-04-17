# Напишите программу, которая создает 2 потока. В первом потоке будет выполняться функция, которая выводит числа от 1 до 5, во втором - функция, которая будет выводить буквы от a до e (англ.).
# Дождитесь выполнения обоих потоков и затем выведите в консоль Готово!.
# Для создания и запуска потоков создайте функцию main() .

import threading


def print_numbers():
    [print(i) for i in range(1, 6)]


def print_letters():
    [print(chr(i)) for i in range(97, 102)]


def main():
    tread_numbers = threading.Thread(target=print_numbers)
    tread_letters = threading.Thread(target=print_letters)

    tread_numbers.start()
    tread_letters.start()

    tread_numbers.join()
    tread_letters.join()

    print("Готово!")


main()
