# Создать и запустить основную корутину.
# Внутри основной корутины создать задачу для каждого файла из списка files с использованием встроенной в данное задание корутины download_file(file_name).
# Найти все исключения, возникшие в процессе скачивания файла, и вывести их на экран в произвольном порядке (выводить только исключения, сообщения об успешном скачивании файла выводить не нужно). Можете использовать для решения задачи разные способы работы с исключениями:
# asyncio.gather(return_exceptions=)
# asyncio.wait() c task.exception()...
# Обратите внимание, что время выполнения задания ограничено, поэтому запускайте скачивание всех файлов конкурентно.


async def main() -> None:
    tasks = [asyncio.create_task(download_file(file_name)) for file_name in files]

    await asyncio.gather(*tasks, return_exceptions=True)

    [
        print(task.exception(), sep="\n")
        for task in tasks
        if task.exception() is not None
    ]


asyncio.run(main())
