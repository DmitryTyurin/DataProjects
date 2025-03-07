# Реализовать асинхронную функцию обработки загрузки и конвертации файлов, которая будет управлять количеством одновременно конвертируемых файлов с использованием семафоров.
# В зависимости от типа аккаунта необходимо ограничить количество одновременно выполняемых задач конвертации.

import asyncio

files = input().split()
account_type = input().strip().lower()


async def convert_file(file: str, semaphore: asyncio.BoundedSemaphore) -> str:
    async with semaphore:
        await asyncio.sleep(1)
        return f"Файл {file} обработан"


async def main() -> None:
    try:
        semaphore = (
            asyncio.BoundedSemaphore(10)
            if account_type == "premium"
            else asyncio.BoundedSemaphore(2)
        )
        async with asyncio.TaskGroup() as tg:
            results = [tg.create_task(convert_file(file, semaphore)) for file in files]

            [print(await result) for result in results]
    except* Exception as e:
        [print(error) for error in e.exceptions]


asyncio.run(main())
