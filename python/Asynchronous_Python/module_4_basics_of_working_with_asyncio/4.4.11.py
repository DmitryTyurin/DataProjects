# Напишите асинхронный код, который запускает два таймера обратного отсчета с разным временем и названиями.
#
# Один таймер - это "Квест на поиск сокровищ", который длится 10 секунд.
# Второй - "Побег от дракона", на выполнение которого дается 5 секунд.
# Используйте asyncio.create_task() для запуска каждого таймера. Таймер должен выводить оставшееся время в сообщениях, примеры которых представлены ниже.

import asyncio
import time

timer = {"Квест на поиск сокровищ": 10, "Побег от дракона": 5}


async def countdown(name: str, seconds: int) -> None:
    for i in range(seconds, 0, -1):
        if name == "Квест на поиск сокровищ":
            print(f"{name}: Осталось {i} сек. Найди скрытые сокровища!")
            await asyncio.sleep(1)
        elif name == "Побег от дракона":
            print(f"{name}: Осталось {i} сек. Беги быстрее, дракон на хвосте!")
            await asyncio.sleep(1)
    print(f"{name}: Задание выполнено! Что дальше?")


async def main() -> None:
    tasks = [
        asyncio.create_task(countdown(name, seconds)) for name, seconds in timer.items()
    ]
    await asyncio.gather(*tasks)


asyncio.run(main())
