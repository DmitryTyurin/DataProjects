# В главной корутине main() используйте asyncio.create_task() для создания трех асинхронных задач. Каждая задача должна запускать функцию counter() , передавая в нее уникальное имя персонажа и задержку.
# Функция counter() должна быть асинхронной (async def). Внутри нее используйте цикл для итерации по списку этапов путешествия и await asyncio.sleep(delay) для создания задержки между этапами.
# После задержки выводите на экран текущий этап путешествия для данного персонажа.
# print(f"{name} {place}...")
# Дождитесь выполнения всех созданных задач в главной корутине с помощью await.

import asyncio

places = [
    "начинает путешествие",
    "находит загадочный лес",
    "переправляется через реку",
    "встречает дружелюбного дракона",
    "находит сокровище",
]

roles = ["Искатель приключений", "Храбрый рыцарь", "Отважный пират"]


async def counter(name: str, delay=0.1) -> None:
    for place in places:
        await asyncio.sleep(delay)
        print(f"{name} {place}...")


async def main() -> None:
    tasks = [asyncio.create_task(counter(role, 0.1)) for role in roles]
    await asyncio.gather(*tasks)


asyncio.run(main())
