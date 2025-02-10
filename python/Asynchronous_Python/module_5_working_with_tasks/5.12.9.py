# Дописать колбэк-функцию on_data_parsed(), которая будет получать результат из задачи, переданной в функцию, и выводить на экран сообщение:
# f"Найдено {len(result)} файлов для скачивания: {result}"
# Внутри корутины parse_data() нужно назначать колбэк для текущей задачи, только если ссылки найдены.
# Сама корутина должна возвращать список найденных ссылок или пустой список, если ссылки не найдены.
# В корутине main() создать задачи для "парсинга" каждого URL-адреса и дождаться выполнения всех задач.


import asyncio
import random

random.seed(5)


def on_data_parsed(task):
    result = task.result()
    if result:
        print(f"Найдено {len(result)} файлов для скачивания: {result}")


async def parse_data(url: str) -> list[str]:
    await asyncio.sleep(1)
    if random.choice([True, False]):
        file_urls = [f"{url}/example_file.zip"]
    else:
        file_urls = []

    if file_urls:
        task = asyncio.current_task()
        task.add_done_callback(on_data_parsed)

    return file_urls


async def main():
    urls = [
        "https://example.com/data1",
        "https://example.com/data2",
        "https://example.com/data3",
    ]

    tasks = [asyncio.create_task(parse_data(url)) for url in urls]

    gather = asyncio.gather(*tasks)
    await gather


asyncio.run(main())
