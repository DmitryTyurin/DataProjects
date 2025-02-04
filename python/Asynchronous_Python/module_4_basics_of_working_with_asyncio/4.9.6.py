# Создайте корутину collect_gold(), которая будет:
# "Собирать" золото от 1 до 5 часов включительно (в коде 1 час равен 1 секунде).
# Возвращать случайное значение собранного золота от 10 до 50 единиц включительно (для получения одинаковых случайных величин и успешного прохождения проверки, значение полученного золота нужно генерировать после "сбора" золота).
# Для генерации случайных значений используйте функцию random.randint() и не меняйте значение random.seed().
# Создайте корутину main(), в которой 10 отрядов будут отправлены на сбор золота.
# После того как каждый отряд завершает сбор, выведите на экран сообщение о собранном золоте и об его общем количестве в следующем формате:


import asyncio
import random

# Не менять!
random.seed(1)


async def collect_gold() -> int:
    await asyncio.sleep(random.randint(1, 5))

    return random.randint(10, 50)


async def main() -> None:
    total_gold = 0

    tasks = [asyncio.create_task(collect_gold(), name=f"Отряд {x}") for x in range(10)]
    completed_tasks = asyncio.as_completed(tasks)

    for task in completed_tasks:
        amount_gold = await task
        total_gold += amount_gold
        print(f"Собрано {amount_gold} единиц золота.")
        print(f"Общее количество золота: {total_gold} единиц.\n")


asyncio.run(main())
