# Откройте сайт, на нём есть 50 ссылок, в каждой ссылке лежит по 10 изображений;
# Ваша задача: Написать асинхронный код который скачает все уникальные изображения которые там есть (они повторяются, а уникальных всего 449) ;
# Вставьте размер всех скачанных изображений в поле для ответа;
# Асинхронный код должен обработать все ссылки и скачать все изображения примерно за 20-30 сек, скорость зависит от скорости вашего интернет соединения.
# Воспользуйтесь функцией ниже, для получения размера всех файлов в папке. Функция на вход принимает путь к папке с изображениями filepath="/img/"

import logging
import aiohttp
import asyncio
from bs4 import BeautifulSoup
import re
import time
import requests


class DataDriver:
    def __init__(self):
        self.base_url = "https://parsinger.ru/asyncio/aiofile/2"
        self.all_urls_list = self.get_all_urls()
        self.max_concurrent_requests = 5
        self.semaphore = asyncio.Semaphore(self.max_concurrent_requests)
        self.dir = "downloaded_images"
        self.dir_size = 0

    def get_html(self):
        response = requests.get(f"{self.base_url}/index.html")
        response.encoding = "utf-8"

        response.raise_for_status()

        if response.status_code == 200:
            return response.text
        else:
            return None  # or raise an exception

    def get_all_urls(self):
        html = self.get_html()
        soup = BeautifulSoup(html, "lxml")

        data = soup.find(name="div", attrs={"class": "item_card"}).find_all(name="a")

        result = [f"{self.base_url}/{item.get("href")}" for item in data]

        return result

    async def fetch_html(self, session, url):
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            else:
                print(f"Ошибка загрузки {url}: статус {response.status}")
                return None

    async def download_image(self, session, url, save_path):
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    content = await response.read()
                    with open(save_path, "wb") as f:
                        f.write(content)
                    print(f"Изображение сохранено: {save_path}")
                else:
                    print(f"Ошибка загрузки {url}: статус {response.status}")
        except Exception as e:
            print(f"Ошибка при загрузке {url}: {str(e)}")

    async def extract_and_download_images(self, session, html, base_url):
        import os
        from urllib.parse import urljoin

        if not html:
            return []

        soup = BeautifulSoup(html, "html.parser")
        img_tags = soup.find_all("img")
        img_urls = [urljoin(base_url, img["src"]) for img in img_tags]

        tasks = []
        for i, img_url in enumerate(img_urls):
            filename = img_url.split("/")[-1]
            save_path = os.path.join(self.dir, filename)

            tasks.append(self.download_image(session, img_url, save_path))

        await asyncio.gather(*tasks)

    async def process_page(self, session, url):
        print(f"Обработка страницы: {url}")
        html = await self.fetch_html(session, url)
        if html:
            await self.extract_and_download_images(session, html, url)

    async def get_and_load_data(self) -> None:
        import os

        if not os.path.exists(self.dir):
            os.makedirs(self.dir)

        async with aiohttp.ClientSession() as session:
            tasks = [self.process_page(session, url) for url in self.all_urls_list]

            await asyncio.gather(*tasks)

    def run_get_and_load_data(self):
        asyncio.run(self.get_and_load_data())

    def get_folder_size(self):
        import os

        for filename in os.listdir(self.dir):
            filepath = os.path.join(self.dir, filename)
            if os.path.isfile(filepath):
                self.dir_size += os.path.getsize(filepath)

        total_size_kb = self.dir_size / 1024
        total_size_mb = total_size_kb / 1024

        print(
            f"Общий размер файлов: {self.dir_size} байт (~{total_size_kb:.2f} KB, ~{total_size_mb:.2f} MB)"
        )

    def os_remove(self):
        import shutil

        try:
            shutil.rmtree(self.dir)
            print(f"Папка {self.dir} успешно удалена")
        except FileNotFoundError:
            print(f"Папка {self.dir} не существует")
        except PermissionError:
            print(f"Нет прав на удаление {self.dir}")
        except Exception as e:
            print(f"Ошибка при удалении: {e}")


def main():
    import time

    start_time = time.perf_counter()

    d = DataDriver()
    d.run_get_and_load_data()
    d.get_folder_size()
    d.os_remove()

    end_time = time.perf_counter()

    print(f"Время выполнения: {end_time - start_time:.2f} секунд")


main()
