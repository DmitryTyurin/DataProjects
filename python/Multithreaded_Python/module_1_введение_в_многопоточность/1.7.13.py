# Цель задачи:
#
# Научиться управлять множеством потоков с разными именами, используя threading.Thread. Задача демонстрирует создание, запуск и синхронизацию потоков, каждый из которых выполняет определенную функцию и имеет уникальное имя.
#
# Ключевые моменты:
#
# Именование потоков: Используется список name_threads = [...], содержащий уникальные идентификаторы. Каждый поток получает имя, основанное на этих идентификаторах (например, 'Name_thread-OF95RK', 'Name_thread-VH61DX' и т.д.).
# ​​​​​​​name_threads = ['OF95RK', 'VH61DX', 'NB03WA', 'WO40ZF', 'NJ48EG', 'SX21ET', 'AT01PA', 'MR36DD', 'DD84HR', 'MI81QY']
# Функция потока: Каждый поток выполняет функцию worker(), которая регистрирует начало работы потока, затем выполняет паузу (сон) на одну секунду (time.sleep(1)) для имитации выполнения работы, и в конце фиксирует завершение работы потока.
# f"{thread_name} начал работу."
# time.sleep(1)
# f"{thread_name} завершил работу."

from threading import Thread, current_thread
import time

name_threads = [
    "OF95RK",
    "VH61DX",
    "NB03WA",
    "WO40ZF",
    "NJ48EG",
    "SX21ET",
    "AT01PA",
    "MR36DD",
    "DD84HR",
    "MI81QY",
]


def worker():
    thread_name = current_thread().name

    print(f"{thread_name} начал работу.")
    time.sleep(1)
    print(f"{thread_name} завершил работу.")


def main():
    threads = [
        Thread(target=worker, name=f"Name_thread-{name_thread}")
        for name_thread in name_threads
    ]

    [thread.start() for thread in threads]

    [thread.join() for thread in threads]


main()
