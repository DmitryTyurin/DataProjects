# Создайте пять задач (по одной на каждый сервер), которые работали бы конкурентно и загружали данные из разных серверов в базу данных.
# В качестве имитации загрузки данных с серверов используйте асинхронную функцию sleep.
# Пусть каждая задача засыпает на случайное значение от 0 до 5, имитируя запрос к базе данных.

import asyncio
import random

SERVERS = {
    "1": "Server_Alpha",
    "2": "Server_Beta",
    "3": "Server_Gamma",
    "4": "Server_Delta",
    "5": "Server_Epsilon",
}


async def load_data(server: str) -> None:
    print(f"Загрузка данных с сервера {server} началась")
    await asyncio.sleep(random.randint(0, 5))

    print(f"Загрузка данных с сервера {server} завершена")


async def main(server_names: dict) -> None:
    try:
        async with asyncio.TaskGroup() as tg:
            [tg.create_task(load_data(name)) for name in server_names.values()]
    except* Exception as e:
        pass


asyncio.run(main(SERVERS))
