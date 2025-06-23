# Откройте сайт, там есть 501 ссылка, секретный код лежит только на четырёх из них;
# Напишите асинхронный код, который найдёт все четыре кода и суммирует их;
# Суммируйте все полученные значения и вставьте результат в поле для ответа:

import logging
import aiohttp
import asyncio
from bs4 import BeautifulSoup
import re
import time
import requests


class DataDriver:
    def __init__(self):
        self.base_url = "https://parsinger.ru/asyncio/create_soup/1/"
        self.all_urls_list = self.get_all_urls()
        self.secret_codes = []
        self.max_concurrent_requests = 100
        self.semaphore = asyncio.Semaphore(self.max_concurrent_requests)

    def get_html(self):
        response = requests.get(f"{self.base_url}/index.html")
        response.encoding = "utf-8"

        response.raise_for_status()

        if response.status_code == 200:
            return response.text
        else:
            return None

    def get_all_urls(self):
        html = self.get_html()
        soup = BeautifulSoup(html, "lxml")

        data = soup.find(name="div", attrs={"class": "item_card"}).find_all(name="a")

        result = [f"{self.base_url}{item.get("href")}" for item in data]

        return result

    async def get_response_using_proxy(self, session, url: str):
        async with self.semaphore:
            try:
                async with session.get(url) as response:
                    html = await response.text()
                    soup = BeautifulSoup(html, "html.parser")

                    div = soup.find(name="p", attrs={"class": "text"}).text

                    result = int(div) if div.isdigit() else 0
                    logging.warning(result)

                    return result

            except Exception as e:
                return 0

    async def get_and_load_data(self) -> None:

        async with aiohttp.ClientSession() as session:
            tasks = [
                self.get_response_using_proxy(session, url)
                for url in self.all_urls_list
            ]

            for task in asyncio.as_completed(tasks):
                result = await task
                self.secret_codes.append(result)

    def run_get_and_load_data(self):
        asyncio.run(self.get_and_load_data())
        print(sum(self.secret_codes))


def main():
    import time

    start_time = time.perf_counter()

    d = DataDriver()
    d.run_get_and_load_data()

    end_time = time.perf_counter()

    print(f"Время выполнения: {end_time - start_time:.2f} секунд")


main()
