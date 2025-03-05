# Цель: Написать асинхронный код, который организует добычу ресурсов (камень, металл, ткань) и последующее производство изделий из них в трех различных цехах.

import asyncio

stone_storage = 0
metal_storage = 0
cloth_storage = 0

stone_resources_dict = {
    "Каменная плитка": 10,
    "Каменная ваза": 40,
    "Каменный столб": 50,
}

metal_resources_dict = {
    "Металлическая цепь": 6,
    "Металлическая рамка": 24,
    "Металлическая ручка": 54,
}

cloth_resources_dict = {
    "Тканевая занавеска": 8,
    "Тканевый чехол": 24,
    "Тканевое покрывало": 48,
}

stone_production_complete = asyncio.Event()
metal_production_complete = asyncio.Event()
cloth_production_complete = asyncio.Event()


async def gather_stone(condition: asyncio.Condition):
    global stone_storage
    while not stone_production_complete.is_set():
        await asyncio.sleep(1)
        stone_storage += 10
        print(f"Добыто 10 ед. камня. На складе {stone_storage} ед.")
        async with condition:
            condition.notify()


async def gather_metal(condition: asyncio.Condition):
    global metal_storage
    while not metal_production_complete.is_set():
        await asyncio.sleep(1)
        metal_storage += 6
        print(f"Добыто 6 ед. металла. На складе {metal_storage} ед.")
        async with condition:
            condition.notify()


async def gather_cloth(condition: asyncio.Condition):
    global cloth_storage
    while not cloth_production_complete.is_set():
        await asyncio.sleep(1)
        cloth_storage += 8
        print(f"Добыто 8 ед. ткани. На складе {cloth_storage} ед.")
        async with condition:
            condition.notify()


async def craft_stone_items(condition: asyncio.Condition):
    global stone_storage
    for item, required_stone in stone_resources_dict.items():
        async with condition:
            while stone_storage < required_stone:
                await condition.wait()
            stone_storage -= required_stone
            print(f"Изготовлен {item} из камня.")
    stone_production_complete.set()


async def craft_metal_items(condition: asyncio.Condition):
    global metal_storage
    for item, required_metal in metal_resources_dict.items():
        async with condition:
            while metal_storage < required_metal:
                await condition.wait()
            metal_storage -= required_metal
            print(f"Изготовлен {item} из металла.")
    metal_production_complete.set()


async def craft_cloth_items(condition: asyncio.Condition):
    global cloth_storage
    for item, required_cloth in cloth_resources_dict.items():
        async with condition:
            while cloth_storage < required_cloth:
                await condition.wait()
            cloth_storage -= required_cloth
            print(f"Изготовлен {item} из ткани.")
    cloth_production_complete.set()


async def main():
    condition = asyncio.Condition()

    gather_stone_task = asyncio.create_task(gather_stone(condition))
    gather_metal_task = asyncio.create_task(gather_metal(condition))
    gather_cloth_task = asyncio.create_task(gather_cloth(condition))

    craft_stone_task = asyncio.create_task(craft_stone_items(condition))
    craft_metal_task = asyncio.create_task(craft_metal_items(condition))
    craft_cloth_task = asyncio.create_task(craft_cloth_items(condition))

    await asyncio.gather(
        gather_stone_task,
        gather_metal_task,
        gather_cloth_task,
        craft_stone_task,
        craft_metal_task,
        craft_cloth_task,
    )


asyncio.run(main())
