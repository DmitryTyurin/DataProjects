# Структура CSV файла проста, число, которое вам нужно суммировать, находится в ячейке "1а".
# Это означает, что это число находится в первом столбце (столбец "a") и на первой строке (строка "1") каждого CSV файла.

import asyncio
import aiofiles
import csv
import os
from pathlib import Path


async def read_csv(file_path, semaphore):
    async with semaphore:
        async with aiofiles.open(file_path, mode="r") as file:
            content = await file.read()
            reader = csv.reader(content.splitlines())
            first_row = next(reader)
            number = float(first_row[0])
            return number


def find_csv_files(directory):
    csv_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
                csv_files.append(Path(root) / file)
    return csv_files


async def process_files(csv_files, semaphore):
    tasks = [asyncio.create_task(read_csv(file, semaphore)) for file in csv_files]
    numbers = await asyncio.gather(*tasks)
    return sum(numbers)



async def main():
    directory = "5000folder"
    semaphore = asyncio.Semaphore(100)

    csv_files = find_csv_files(directory)

    total_sum = await process_files(csv_files, semaphore)
    print(total_sum)


asyncio.run(main())
