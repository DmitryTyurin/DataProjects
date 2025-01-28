# Создайте корутину print_with_delay(), которая принимает целое число в качестве аргумента и выводит сообщение следующего типа:
#
# f'Coroutine {num} is done'
# Используя только что созданную корутину, создайте 10 задач (tasks) для асинхронного выполнения.
# При создании каждой задачи передавайте в print_with_delay() числа от 0 до 9.

import asyncio


async def print_with_delay(num: int) -> None:
    await asyncio.sleep(1)
    print(f"Coroutine {num} is done")


async def main() -> None:
    tasks = [asyncio.create_task(print_with_delay(i)) for i in range(10)]
    await asyncio.gather(*tasks)


asyncio.run(main())
