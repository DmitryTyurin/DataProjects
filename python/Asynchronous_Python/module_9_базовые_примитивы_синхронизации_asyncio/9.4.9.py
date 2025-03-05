# Ваша задача - написать асинхронный код, который моделирует доступ пользователей к базе данных.
# Все запросы должны быть обработаны в порядке очереди.

import asyncio

users = [
    "Alice",
    "Bob",
    "Charlie",
    "Dave",
    "Eva",
    "Frank",
    "George",
    "Helen",
    "Ivan",
    "Julia",
]


async def user(name: str, condition: asyncio.Condition) -> None:
    print(f"Пользователь {name} ожидает доступа к базе данных")

    async with condition:
        await condition.wait()
        print(f"Пользователь {name} подключился к БД")

        await asyncio.sleep(1)
        print(f"Пользователь {name} отключается от БД")

        condition.notify()


async def controller(condition: asyncio.Condition) -> None:
    for user in users:
        async with condition:
            condition.notify()
            await asyncio.sleep(0)


async def main() -> None:
    condition = asyncio.Condition()

    user_tasks = [asyncio.create_task(user(name, condition)) for name in users]
    controller_task = asyncio.create_task(controller(condition))

    await asyncio.gather(*user_tasks, controller_task)


asyncio.run(main())
