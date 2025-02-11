# Задание: Написать код, который будет моделировать шоу с фейерверками, используя все возможные комбинации форм, цветов и действий.
# Каждый фейерверк представляет собой уникальную комбинацию этих характеристик.
# Ваша задача - написать асинхронный код, который имитирует запуск каждого фейерверка и затем выводит сообщение о его завершении.

import asyncio
import itertools
import random

SHAPES = ["circle", "star", "square", "diamond", "heart"]
COLORS = ["red", "blue", "green", "yellow", "purple"]
ACTIONS = ["change_color", "explode", "disappear"]


async def launch_fireworks(fire_combination: tuple) -> None:
    shape, color, action = fire_combination
    print(f"Запущен {color} {shape} салют, в форме {action}!!!")

    await asyncio.sleep(random.randint(1, 5))
    print(f"Салют {color} {shape} завершил выступление {action}")


async def main(shapes: list, colors: list, actions: list) -> None:
    combinations = list(itertools.product(shapes, colors, actions))

    try:
        async with asyncio.TaskGroup() as tg:
            [
                tg.create_task(launch_fireworks(fire_combination))
                for fire_combination in combinations
            ]
    except* Exception as e:
        pass


asyncio.run(main(SHAPES, COLORS, ACTIONS))
