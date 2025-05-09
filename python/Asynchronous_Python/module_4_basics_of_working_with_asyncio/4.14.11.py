# Блокирующая функция blocking_func(), способная заблокировать работу вашего приложения на долгие 3 секунды.
# Приложение, выполняющее асинхронно две задачи.
# Необходимо:
#
# Дописать код, который позволит запустить blocking_func() в потоке, отдельном от основного потока исполнения:
# # Создайте корутину для запуска blocking_func() в независимом потоке:
# new_coro =
# Получить номера потоков для основного потока (main()):
# # Получите идентификатор текущего потока!!!
# base_thread_id =
# и для потока, в котором будет запущена blocking_func():
# # Получите идентификатор текущего потока!!!
# new_thread_id =
# Для получения идентификатора потока используйте threading.current_thread().ident библиотеки threading
# Внимание!
#
# Все необходимые библиотеки уже импортированы!
# Используемые в программе переменные и названия функций — не переименовывать!
# Будьте внимательны при передаче функции в asyncio.to_thread()!

import time
import asyncio
import threading

base_thread_id = 0
new_thread_id = 0


# Блокирующая функция
def blocking_func():
    global new_thread_id
    # Получите идентификатор текущего потока!!!
    new_thread_id = threading.current_thread().ident
    # Печать сообщения о старте и номере используемого потока.
    print(f"Старт blocking_func() в потоке c id {new_thread_id}")
    # Имитация выполнения долгой блокирующей IO-bound операции
    time.sleep(3)
    # Печать сообщения о завершении работы
    print("blocking_func() успешно выполнена!")


# Первая корутина
async def coro1():
    # Имитация выполнения IO-bound операции
    await asyncio.sleep(1)
    print("Выполнение coro1 завершено!")


# Вторая корутина
async def coro2():
    # Имитация выполнения IO-bound операции
    await asyncio.sleep(2)
    print("Выполнение coro2 завершено!")


async def main():
    global base_thread_id
    # Получите идентификатор текущего потока!!!
    base_thread_id = threading.current_thread().ident
    # Печать сообщения о старте и номере используемого потока
    print(f"Идентификатор основного потока {base_thread_id}")
    # Создайте корутину для запуска blocking_func() в независимом потоке:
    new_coro = asyncio.to_thread(blocking_func)
    # Асинхронный запуск задач.
    await asyncio.gather(new_coro, coro1(), coro2())


asyncio.run(main())
