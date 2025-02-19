# Ваша задача — модифицировать исходный код так, чтобы устранить проблему условий гонки с помощью асинхронного замка asyncio.Lock().
# Код должен вывести корректное значение global_counter.

import asyncio

global_counter = 0
lock = asyncio.Lock()


async def increment():
    async with lock:
        global global_counter
        temp = global_counter
        await asyncio.sleep(0.01)
        global_counter = temp + 2.39


async def main():
    await asyncio.gather(*[increment() for x in range(99)])


asyncio.run(main())
print(f"global_counter: {round(global_counter,2)}")
