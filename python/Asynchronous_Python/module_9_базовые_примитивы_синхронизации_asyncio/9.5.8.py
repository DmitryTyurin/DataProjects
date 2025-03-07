# Ваша задача - разработать систему, которая позволит контролировать поток запросов от пользователей, чтобы избежать перегрузки сервера.
# Эта система должна обеспечивать выполнение не более трех запросов одновременно, остальные должны ожидать своей очереди.

import asyncio

users = [
    "sasha",
    "petya",
    "masha",
    "katya",
    "dima",
    "olya",
    "igor",
    "sveta",
    "nikita",
    "lena",
    "vova",
    "yana",
    "kolya",
    "anya",
    "roma",
    "nastya",
    "artem",
    "vera",
    "misha",
    "liza",
]

semaphore = asyncio.Semaphore(3)
requests = 0


async def send_request(user: str) -> None:
    global requests

    async with semaphore:
        print(f"Пользователь {user} делает запрос")

        await asyncio.sleep(1)

        requests += 1
        print(f"Запрос от пользователя {user} завершен")
        print(f"Всего запросов: {requests}")


async def main() -> None:
    try:
        async with asyncio.TaskGroup() as tg:
            [tg.create_task(send_request(user)) for user in users]
    except* Exception as e:
        [print(error) for error in e.exceptions]


asyncio.run(main())
