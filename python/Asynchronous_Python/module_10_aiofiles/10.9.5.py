# Помните, что ключ к успеху в этой задаче - асинхронное программирование.
# Это позволит вашему коду эффективно обрабатывать большие объемы данных без блокировки основного потока приложения.
# Ваша цель: разработать функцию, которая будет асинхронно читать данные из CSV-файла, а затем записывать их в JSON-файл.


import asyncio
import aiofiles
import csv
import json
import aiocsv


async def convert_csv_to_json(csv_filename, json_filename):
    """
    Асинхронная функция для преобразования данных из CSV в JSON.
    :param csv_filename: путь до CSV-файла
    :param json_filename: путь до JSON-файла
    """
    try:
        async with aiofiles.open(
            csv_filename, mode="r", encoding="utf-8-sig"
        ) as csv_file:
            async_reader = aiocsv.AsyncDictReader(csv_file, delimiter=";")
            data = [row async for row in async_reader]

        async with aiofiles.open(
            json_filename, mode="w", encoding="utf-8"
        ) as json_file:
            await json_file.write(json.dumps(data, ensure_ascii=False, indent=4))

        print(
            f"Преобразование завершилось успешно! Данные сохранены в {json_filename}."
        )

    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Основная функция
async def main():
    file_name = "address_10000"

    csv_file_path = f"{file_name}.csv"
    json_file_path = f"{file_name}.json"

    await convert_csv_to_json(csv_file_path, json_file_path)


asyncio.run(main())
