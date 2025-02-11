# Создать и запустить основную корутину.
# Внутри основной корутины создать задачу для каждого файла из списка files с использованием встроенной в данное задание корутины download_file(file_name).
# Найти все исключения, возникшие в процессе скачивания файла, и вывести их на экран в произвольном порядке (выводить только исключения, сообщения об успешном скачивании файла выводить не нужно).
# Для решения задачи надо использовать TaskGroup
# Обратите внимание, что время выполнения задания ограничено, поэтому запускайте скачивание всех файлов конкурентно.

import asyncio


async def main() -> None:
    try:
        async with asyncio.TaskGroup() as tg:
            [tg.create_task(download_file(file_name)) for file_name in files]

    except* Exception as e:
        [print(error) for error in e.exceptions]


asyncio.run(main())
