# Представьте, что вы работаете в большой компании, которая обрабатывает огромное количество данных каждый день.
# Ваши данные хранятся в отдельных файлах(*.txt), и каждый файл содержит одно число(от 1 до 99).
# Ваша задача - написать эффективный код, который быстро обрабатывает эти файлы и суммирует все четные числа.
# Важно, что файлы должны быть прочитаны асинхронно, чтобы увеличить производительность.


import asyncio
import aiofiles
from aiofiles import os as aio_os


async def read_file(file_path, semaphore):
    async with semaphore:
        async with aiofiles.open(file_path, mode="r") as file:
            content = await file.read()
            number = int(content.strip())
            return number


async def process_files(directory):
    files = await aio_os.listdir(directory)
    semaphore = asyncio.Semaphore(100)
    tasks = []

    for file_name in files:
        if file_name.endswith(".txt"):
            file_path = f"{directory}/{file_name}"
            task = asyncio.create_task(read_file(file_path, semaphore))
            tasks.append(task)

    numbers = await asyncio.gather(*tasks)
    return numbers


def sum_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)


async def main():
    directory = "files"  # Укажите путь к директории с файлами
    numbers = await process_files(directory)
    total_sum = sum_even_numbers(numbers)
    print(total_sum)


asyncio.run(main())
