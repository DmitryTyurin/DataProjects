# Один любитель компьютерных игр поставил себе цель пройти компанию в его любимой игре за 24 часа.
# Каждый час в игре происходило автосохранение.
# Игрок почти не ошибался, но все же несколько раз не справился с заданиями, и пришлось загружать последнюю версию сохраненной игры.
# Общее время прохождения составило 20 часов 30 минут.


import asyncio


async def autosave(queue):
    for time in range(1, 21):
        await asyncio.sleep(0.1)

        await queue.put(f"Автосохранение {time}")
        print(f"Автосохранение игры через {time} часов")


async def simulate_gameplay(queue):
    for time in range(1, 21):
        await asyncio.sleep(0.1)

        if time % 5 == 0:
            autosave = await queue.get()
            print(f"Загружена последняя версия игры: {autosave}")

    print("Игра пройдена!")


async def main():
    queue = asyncio.LifoQueue()

    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(autosave(queue))
            tg.create_task(simulate_gameplay(queue))

    except* Exception as e:
        [print(error) for error in e.exceptions]


asyncio.run(main())
