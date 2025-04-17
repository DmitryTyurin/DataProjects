# Описание задачи:
# Напишите программу для имитации параллельной загрузки, обработки и сохранения серии файлов, используя многопоточность. Для каждого файла необходимо выполнить три этапа работы: загрузка, обработка и сохранение. Каждый этап должен выполняться в отдельном потоке со своим названием.
#
# Вы должны создать отдельные функции для каждого этапа работы с файлом:
#
# load_file() — Для имитации загрузки файла,
# process_file() — Для обработки файла,
# save_file() — Для имитации сохранения файла.
# Каждая функция должна имитировать свою работу с помощью паузы time.sleep(), чтобы представить время, затрачиваемое на каждую операцию.
#
# Пример функции load_file():
#
# f"{thread_name} начал загрузку файла {file_name}."
# time.sleep(1)   # Имитация процесса загрузки файла
# f"{thread_name} завершил загрузку файла {file_name}."
# Важным аспектом задачи является использование именованных потоков. Для каждого файла и каждой операции создайте отдельный поток с уникальным именем, отражающим операцию и имя файла, например, LoadThread-file623.xlsx, ProcessThread-file538.jpg, SaveThread-file11.rar.
#
# file_names = ['file623.xlsx', 'file538.jpg', ..., 'file13.txt']
# Для каждого файла из этого списка создается тройка потоков (для загрузки, обработки и сохранения). После создания все потоки запускаются, и программа дожидается их завершения.
#
# Формирование Имени Потоков:
#
# Имена потоков должны формироваться по следующему принципу:
# Для потока загрузки: "LoadThread-{file_name}", где {file_name} — имя файла из списка file_names = [].
# Для потока обработки: "ProcessThread-{file_name}".
# Для потока сохранения: "SaveThread-{file_name}".
# Пример: Если имя файла file123.txt, то соответствующие имена потоков будут LoadThread-file123.txt, ProcessThread-file123.txt и SaveThread-file123.txt.
# Полный список имён file_names=[] вшит в задачу, вставлять его в поле ответа не обязательно.
# Каждая строка вывода должна быть на новой строке.
# Вывод программы должен быть следующий:
#
# res = []
# ...
# ...
# ...
#
# for x in res:
#     print(x)
# LoadThread-file623.xlsx начал загрузку файла file623.xlsx.
# ProcessThread-file623.xlsx начал обработку файла file623.xlsx.
# SaveThread-file623.xlsx начал сохранение файла file623.xlsx.
# ...
# ...
# ...
# ProcessThread-file566.jpg завершил обработку файла file566.jpg.
# ProcessThread-file66.rar завершил обработку файла file66.rar.
# ProcessThread-file13.txt завершил обработку файла file13.txt.
#
#
# Внимание! Важно!
# Используйте список res=[] для наполнения строками, а в конце кода выводите его содержимое с помощью цикла for.
# Обычные принты из функций задача может не засчитать!

import threading
import time

file_names = [
    "file623.xlsx",
    "file538.jpg",
    "file11.rar",
    "file180.jpg",
    "file984.docx",
    "file931.rar",
    "file600.zip",
    "file928.jpg",
    "file899.pdf",
    "file763.png",
    "file601.txt",
    "file194.pdf",
    "file307.rar",
    "file961.jpg",
    "file539.mp4",
    "file44.docx",
    "file276.zip",
    "file387.zip",
    "file520.xlsx",
    "file516.mp3",
    "file802.jpg",
    "file708.mp3",
    "file100.xlsx",
    "file327.xlsx",
    "file451.zip",
    "file125.pdf",
    "file477.jpg",
    "file432.pdf",
    "file569.docx",
    "file990.mp3",
    "file688.mp3",
    "file735.docx",
    "file505.txt",
    "file650.docx",
    "file445.png",
    "file963.mp4",
    "file583.pdf",
    "file403.xlsx",
    "file406.pdf",
    "file187.txt",
    "file13.zip",
    "file495.docx",
    "file47.png",
    "file491.rar",
    "file506.zip",
    "file960.docx",
    "file95.mp3",
    "file566.jpg",
    "file66.rar",
    "file13.txt",
]

res = []


class ETL:
    def __init__(self, file_name):
        self.file_name = file_name

    def load_file(self):
        thread_name = threading.current_thread().name
        res.append(f"{thread_name} начал загрузку файла {self.file_name}.")
        time.sleep(1)  # Имитация загрузки
        res.append(f"{thread_name} завершил загрузку файла {self.file_name}.")

    def process_file(self):
        thread_name = threading.current_thread().name
        res.append(f"{thread_name} начал обработку файла {self.file_name}.")
        time.sleep(1)  # Имитация обработки
        res.append(f"{thread_name} завершил обработку файла {self.file_name}.")

    def save_file(self):
        thread_name = threading.current_thread().name
        res.append(f"{thread_name} начал сохранение файла {self.file_name}.")
        time.sleep(1)  # Имитация сохранения
        res.append(f"{thread_name} завершил сохранение файла {self.file_name}.")


def main():
    threads = []

    for file_name in file_names:
        etl = ETL(file_name)

        load_thread = threading.Thread(
            target=etl.load_file, name=f"LoadThread-{file_name}"
        )
        process_thread = threading.Thread(
            target=etl.process_file,
            name=f"ProcessThread-{file_name}",
        )
        save_thread = threading.Thread(
            target=etl.save_file, name=f"SaveThread-{file_name}"
        )

        threads.extend([load_thread, process_thread, save_thread])

    [thread.start() for thread in threads]

    [thread.join() for thread in threads]


main()
[print(x) for x in res]
