# Описание задачи:
#
# Напишите программу, использующую потоки для сортировки трех различных массивов.
#
# array_descending = [544, 733, 345, 496, 448, 239, 526, 606, 725, 389]
# array_ascending = [428, 419, 760, 124, 662, 168, 829, 501, 350, 389]
# symbols_array = ['b', 'q', 'k', 'd', 'e', 'z', 'n', 'o', 'h', 's', 'm', 'l', 'g', 'a', 'w']
# В программе должны быть три потока (thread1, thread2, thread3): первый поток сортирует массив чисел в порядке убывания, второй поток сортирует другой массив чисел в порядке возрастания, а третий поток сортирует массив символов в лексикографическом порядке. Каждый поток работает со своим массивом независимо от других. После завершения работы всех потоков, основной поток выводит отсортированные массивы.
#
# # Выводим отсортированные массивы
# print(f"Массив чисел (по убыванию): {array_descending}")
# print(f"Массив чисел (по возрастанию): {array_ascending}")
# print(f"Массив символов (лексикографический порядок): {symbols_array}")
# Требования к выводу: Программа должна выводить три отсортированных массива: первый массив чисел в порядке убывания, второй массив чисел в порядке возрастания и третий массив символов в лексикографическом порядке.


import threading

# Глобальные переменные для массивов
array_descending = [733, 725, 389, 606, 544, 526, 496, 448, 345, 239]
array_ascending = [124, 168, 350, 501, 389, 419, 428, 662, 760, 829]
symbols_array = [
    "g",
    "e",
    "k",
    "a",
    "w",
    "z",
    "o",
    "b",
    "m",
    "l",
    "h",
    "n",
    "d",
    "s",
    "q",
]


# Функции для сортировки массивов
def sort_numbers_descending() -> None:
    global array_descending

    array_descending.sort(reverse=True)


def sort_numbers_ascending() -> None:
    global array_ascending

    array_ascending.sort()


def sort_symbols() -> None:
    global symbols_array

    symbols_array.sort()


# Создайте и запустите потоки для сортировки
thread1 = threading.Thread(target=sort_numbers_descending)
thread2 = threading.Thread(target=sort_numbers_ascending)
thread3 = threading.Thread(target=sort_symbols)

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

# Выведете отсортированные массивы
print(f"Массив чисел (по убыванию): {array_descending}")
print(f"Массив чисел (по возрастанию): {array_ascending}")
print(f"Массив символов (лексикографический порядок): {symbols_array}")
