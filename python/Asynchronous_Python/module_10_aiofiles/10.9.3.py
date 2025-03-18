# Ваша задача - прочитать все CSV файлы, содержащиеся в архиве, и суммировать все числа, которые хранятся в этих файлах.
# Это означает, что вы должны пройти по всем файлам в архиве, открыть каждый из них, прочитать данные и суммировать все числа.
# Важно, чтобы ваш код был асинхронным, чтобы вы могли обрабатывать несколько файлов одновременно и ускорить процесс обработки данных.

import asyncio
import aiofiles
from aiofiles import os as aio_os
import csv


async def read_csv(file_path):
    async with aiofiles.open(file_path, mode='r') as file:
        content = await file.read()
        reader = csv.reader(content.splitlines())
        first_row = next(reader)
        number = float(first_row[0])
        return number


async def process_files(directory):
    files = await aio_os.listdir(directory)
    semaphore = asyncio.Semaphore(10)
    tasks = []

    for file_name in files:
        if file_name.endswith(".csv"):
            file_path = f"{directory}/{file_name}"
            task = asyncio.create_task(read_csv(file_path))
            tasks.append(task)

    numbers = await asyncio.gather(*tasks)
    return numbers


def sum_even_numbers(numbers):
    return sum(numbers)


async def main():
    directory = "5000csv"
    numbers = await process_files(directory)
    total_sum = sum_even_numbers(numbers)
    print(total_sum)


asyncio.run(main())