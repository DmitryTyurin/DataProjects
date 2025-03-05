# Создать асинхронный код, который реализует взаимодействие между двумя корутинами: одной, которая добывает древесину, и другой, которая изготавливает предметы из этой древесины.

import asyncio

wood_resources_dict = {
    "Деревянный меч": 6,
    "Деревянный щит": 12,
    "Деревянный стул": 24,
}

storage: int = 0
production_complete: asyncio.Event = asyncio.Event()


async def gather_wood(condition: asyncio.Condition) -> None:
    global storage

    while not production_complete.is_set():
        await asyncio.sleep(1)

        storage += 2
        print(f"Добыто 2 ед. дерева. На складе {storage} ед.")

        async with condition:
            condition.notify()


async def craft_item(condition: asyncio.Condition, wood_resources_dict: dict) -> None:
    global storage

    for item, required_wood in wood_resources_dict.items():
        async with condition:
            while storage < required_wood:
                await condition.wait()

            storage -= required_wood
            print(f"Изготовлен {item}.")

    production_complete.set()


async def main() -> None:
    condition = asyncio.Condition()

    gather_task = asyncio.create_task(gather_wood(condition))
    craft_task = asyncio.create_task(craft_item(condition, wood_resources_dict))

    await asyncio.gather(gather_task, craft_task)


asyncio.run(main())
