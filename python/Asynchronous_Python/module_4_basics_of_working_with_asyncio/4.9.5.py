# Напишите асинхронную функцию upload_file(filename, delay), которая будет симулировать загрузку фильма на сервер, "засыпая" на время delay секунд, а затем возвращая название файла.
# Данная функция не должна выводить ничего на экран.
# В корутине main() запустите задачи по скачиванию всех фильмов. Далее по мере завершения загрузки каждого фильма выводите на экран сообщение в формате: "{filename}: фильм загружен на сервер".


import asyncio

files = {
    "Начало": 4.2,
    "Матрица": 3.8,
    "Аватар": 5.1,
    "Интерстеллар": 2.6,
    "Паразиты": 6.0,
    "Джокер": 4.5,
    "Довод": 3.3,
    "Побег из Шоушенка": 5.4,
    "Криминальное чтиво": 2.9,
    "Форрест Гамп": 5.8,
}


async def upload_file(filename: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return filename


async def main() -> None:
    tasks = [
        asyncio.create_task(upload_file(name, delay), name=name)
        for name, delay in files.items()
    ]

    completed_tasks = asyncio.as_completed(tasks)

    for task in completed_tasks:
        result = await task
        print(f"{result}: фильм загружен на сервер")


asyncio.run(main())
