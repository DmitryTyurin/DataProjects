# Дописать корутину main(), добавив в database этап проекта и его статус с использованием контекстного менеджера AsyncListManager.
# Для добавления используйте асинхронный метод stage_append().
# Вывести измененную базу данных на экран после добавления этапа проекта, каждый этап на отдельной строке.
# Вывод на экран нужно делать также из контекстного менеджера.


import asyncio

async def main():
    new_item = input().split(", ")

    new_item = {"название": new_item[0], "статус": new_item[1]}

    async with AsyncListManager() as manager:
        await manager.stage_append(new_item)

        [print(x) for x in database]


asyncio.run(main())
