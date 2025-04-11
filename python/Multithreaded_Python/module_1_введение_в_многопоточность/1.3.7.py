# Напишите программу, которая создает 2 потока. Первый поток должен вычислять сумму всех чисел от 1 до 1000, а второй поток — произведение всех чисел от 1 до 10. После завершения работы обоих потоков выведите полученные сумму и произведение.
#
# Для вывода результатов используйте:
#
# print(f"Сумма чисел от 1 до 1000: {...}")
# print(f"Произведение чисел от 1 до 10: {...}")
# Примечание: При создании потока используйте параметр args для передачи аргументов целевой функции.

import threading


def sum_numbers(start: int, end: int) -> None:
    result = sum(range(start, end + 1))

    print(f"Сумма чисел от {start} до {end}: {result}")


def product_numbers(start: int, end: int) -> None:
    result = 1
    for i in range(start, end + 1):
        result *= i

    print(f"Произведение чисел от {start} до {end}: {result}")


if __name__ == "__main__":
    sum_thread = threading.Thread(target=sum_numbers, args=(1, 1000))
    product_thread = threading.Thread(target=product_numbers, args=(1, 10))

    sum_thread.start()
    product_thread.start()

    sum_thread.join()
    product_thread.join()
