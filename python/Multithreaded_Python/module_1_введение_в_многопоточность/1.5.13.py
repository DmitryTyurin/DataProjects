# Напишите программу, которая создает 2 потока. В первый поток передайте целевую функцию, которая будет выводить числа от 1 до 5 с интервалом в 0.5 секунд,
# а во второй — целевую функцию, которая будет выводить числа от 6 до 10 с интервалом 1 секунды.
# Дождитесь завершения работы обоих потоков и в главном потоке выведите:
#
# Оба потока завершили свою работу.

import threading
import time


def print_nums(start: int, end: int, time_sleep: int):
    [print(i) or time.sleep(time_sleep) for i in range(start, end)]


t1 = threading.Thread(target=print_nums, args=(1, 6, 0.5))
t2 = threading.Thread(target=print_nums, args=(6, 11, 1))

t1.start()
t2.start()

t1.join()
t2.join()

print("Оба потока завершили свою работу.")
