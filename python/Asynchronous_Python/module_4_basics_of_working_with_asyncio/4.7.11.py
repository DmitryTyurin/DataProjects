# Создайте 20 асинхронных задач, по одной для каждого бегуна, где каждая задача будет симулировать время, необходимое бегуну для завершения забега.
# Используйте функцию asyncio.create_task() для инициализации каждой задачи, asyncio.wait_for()
# для установки максимального времени выполнения всех задач и asyncio.gather() для одновременного старта бегунов.

import asyncio

RUNNERS = {
    "Молния Марк": 12.8,
    "Ветреный Виктор": 13.5,
    "Скоростной Степан": 11.2,
    "Быстрая Белла": 10.8,
}

DISTANCE = 100


async def run_lap(name: str, speed: float) -> None:
    time_needed = DISTANCE / speed

    await asyncio.sleep(time_needed)
    print(f"{name} завершил круг за {round(time_needed, 2)} секунд")


async def main(max_time=10) -> None:
    tasks = [
        asyncio.create_task(run_lap(name, speed)) for name, speed in RUNNERS.items()
    ]
    try:
        await asyncio.wait_for(asyncio.gather(*tasks), max_time)
    except asyncio.TimeoutError:
        pass


asyncio.run(main())
