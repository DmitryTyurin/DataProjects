# Ваша задача: Создать программу, запускающую 5 роботов, двигающихся асинхронно к позиции "A", и считающую количество обращений к этому месту.

import asyncio

robot_names = ["Электра", "Механикс", "Оптимус", "Симулакр", "Футуриус"]
counter = 0


async def visit_robot(lock):
    global counter

    async with lock:
        for index, robot_name in enumerate(robot_names):
            counter += 1

            print(f"Робот {robot_name}({index}) передвигается к месту A")
            await asyncio.sleep(0.5)

            print(
                f"Робот {robot_name}({index}) достиг места A. Место A посещено {counter} раз"
            )
            await asyncio.sleep(1)


async def main():
    lock = asyncio.Lock()

    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(visit_robot(lock))

    except* Exception as e:
        [print(error) for error in e.exceptions]


asyncio.run(main())
