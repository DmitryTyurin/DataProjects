# Напишите код для параллельной загрузки текстовых файлов из списка URL-адресов. Программа должна определить и вывести имя первого успешно скачанного файла, используя функцию as_completed.
#
# Подготовка списка URL-адресов:
#
# Имеется список URL-адресов, каждый из которых ведет к текстовому файлу. Эти файлы будут объектами загрузки в вашей программе.
# urls = ['https://asyncio.ru/multithreading/zadachi/6.2/1/1XhKkbDD.txt',
#         'https://asyncio.ru/multithreading/zadachi/6.2/1/7S2gWnLv.txt',
#         'https://asyncio.ru/multithreading/zadachi/6.2/1/g277YKL0.txt',
#         'https://asyncio.ru/multithreading/zadachi/6.2/1/I1HtO6Mq.txt',
#         'https://asyncio.ru/multithreading/zadachi/6.2/1/IhOYyvOe.txt',
#         'https://asyncio.ru/multithreading/zadachi/6.2/1/M1wlL6jq.txt',
#         'https://asyncio.ru/multithreading/zadachi/6.2/1/M3ifGSqg.txt',
#         'https://asyncio.ru/multithreading/zadachi/6.2/1/tEWbv18D.txt',
#         'https://asyncio.ru/multithreading/zadachi/6.2/1/usMtkqVB.txt',
#         'https://asyncio.ru/multithreading/zadachi/6.2/1/x2Ifki9M.txt']
# В списке urls = [] имеется неизвестное количество неработающих ссылок, ваш код должен обработать или игнорировать их.
# Напишите функцию для загрузки файла:
#
# Напишите функцию download_file(url), которая принимает URL в качестве аргумента.
# Функция должна извлекать имя файла из URL, скачивать файл и сохранять его локально.
# В случае успеха, функция возвращает имя файла. В случае ошибки, возвращает сообщение об ошибке.
# Использование ThreadPoolExecutor для параллельной загрузки:
#
# Инициализируйте ThreadPoolExecutor с определенным количеством рабочих потоков (рекомендуется, 10).
# Используйте метод submit() для отправки задачи загрузки каждого файла в пул потоков. Сохраните возвращаемые объекты Future в словаре или другой структуре данных.
# Применение as_completed() для отслеживания завершения задач:
#
# Итерируйтесь через объекты Future, используя as_completed, чтобы получить результаты задач по мере их завершения.
# Проверьте результат каждой задачи. Если задача успешно завершилась и вернула имя файла, выведите это имя и прервите цикл, чтобы не ждать остальные загрузки.
# Вывод результатов:
#
# Ваш код должен вывести имя первого скачанного файла с применением функции as_completed().
# Вывод должен быть следующим:
# Первый скачанный файл: ***.txt
#
# print(f"Первый скачанный файл: {file_name}")
# Вставьте текст и имя файла в поле ответа на Степик, как показано выше.
# Вставить нужно не код, а строку, т.е имя файла.

from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import os
from urllib.parse import urlparse

urls = [
    "https://asyncio.ru/multithreading/zadachi/6.2/1/1XhKkbDD.txt",
    "https://asyncio.ru/multithreading/zadachi/6.2/1/7S2gWnLv.txt",
    "https://asyncio.ru/multithreading/zadachi/6.2/1/g277YKL0.txt",
    "https://asyncio.ru/multithreading/zadachi/6.2/1/I1HtO6Mq.txt",
    "https://asyncio.ru/multithreading/zadachi/6.2/1/IhOYyvOe.txt",
    "https://asyncio.ru/multithreading/zadachi/6.2/1/M1wlL6jq.txt",
    "https://asyncio.ru/multithreading/zadachi/6.2/1/M3ifGSqg.txt",
    "https://asyncio.ru/multithreading/zadachi/6.2/1/tEWbv18D.txt",
    "https://asyncio.ru/multithreading/zadachi/6.2/1/usMtkqVB.txt",
    "https://asyncio.ru/multithreading/zadachi/6.2/1/x2Ifki9M.txt",
]


class DataDownloader:
    def __init__(self, urls):
        self.urls = urls
        self.executor: ThreadPoolExecutor = ThreadPoolExecutor(max_workers=10)
        self.first_successful_file = None
        self.successful_file_list = []

    def download_file(self, url: str):
        try:
            response = requests.get(url)
            response.raise_for_status()

            file_name = os.path.basename(urlparse(url).path)
            self.successful_file_list.append(file_name)

            with open(file_name, "wb") as file:
                file.write(response.content)

            return file_name
        except requests.exceptions.HTTPError as err:
            print(err)
            return None
        except Exception as err:
            print(err)
            return None

    def run(self):
        with self.executor as executor:
            futures = [executor.submit(self.download_file, url) for url in self.urls]

            for future in as_completed(futures):
                self.first_successful_file = future.result()
                print(f"Первый скачанный файл: {self.first_successful_file}")
                break


downloader = DataDownloader(urls)
downloader.run()
