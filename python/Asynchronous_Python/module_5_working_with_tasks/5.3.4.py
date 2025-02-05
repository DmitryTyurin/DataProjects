# Разработать логику для регулярной проверки и отображения статуса загрузки каждого файла, каждые 1 сек,
# начиная сразу после после запуска задач загрузки файлов.

import asyncio

files = {
    "file1.mp4": 32,
    "image2.png": 24,
    "audio3.mp3": 16,
    "document4.pdf": 8,
    "archive5.zip": 40,
    "video6.mkv": 48,
    "presentation7.pptx": 12,
    "ebook8.pdf": 20,
    "music9.mp3": 5,
    "photo10.jpg": 7,
    "script11.py": 3,
    "database12.db": 36,
    "archive13.rar": 15,
    "document14.docx": 10,
    "spreadsheet15.xls": 25,
    "image16.gif": 2,
    "audioBook17.mp3": 60,
    "tutorial18.mp4": 45,
    "code19.zip": 22,
    "profile20.jpg": 9,
}

NETWORK_SPEED = 8


async def download_file(filename: str, size: int) -> None:
    delay = round(size / NETWORK_SPEED, 3)

    print(
        f"Начинается загрузка файла: {filename}, его размер {size} мб, время загрузки составит {delay} сек"
    )

    await asyncio.sleep(delay)

    print(f"Загрузка завершена: {filename}")


async def monitor_tasks(tasks: list) -> None:
    while True:
        for task in tasks:
            status = task.done()
            print(
                f"Задача {task.get_name()}: {'в процессе' if not status else 'завершена'}, Статус задачи {status}"
            )

        if all(task.done() for task in tasks):
            print("Все файлы успешно загружены")
            break

        await asyncio.sleep(1)


async def main() -> None:
    tasks = [
        asyncio.create_task(download_file(filename, size), name=filename)
        for filename, size in files.items()
    ]

    await monitor_tasks(tasks)


asyncio.run(main())
