# Ниже представлен код, в котором возникает дедлок.
# Ваша задача починить код и сделать так, чтобы программа корректно завершала свое выполнение.

import asyncio

lock = asyncio.Lock()


async def coro(num):
    await asyncio.sleep(num * 0.1)
    print(f"Задача {num} выполнена")


async def main():
    async with asyncio.TaskGroup() as tg:
        [tg.create_task(coro(i)) for i in range(5)]
    print("Работа программы завершена")


asyncio.run(main())
