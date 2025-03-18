# Ваша задача — написать асинхронный код, который обработает все эти страницы и соберёт с них данные, тем самым доказав ему, что страницы в полном порядке.
# Все числа со страниц необходимо просуммировать для выявления возможных отклонений.

import aiohttp
import asyncio
from bs4 import BeautifulSoup

BASE_URL = "https://asyncio.ru/zadachi/2/html/"
MAX_CONCURRENT_REQUESTS = 10

semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)


async def fetch_number(session, url):
    async with semaphore:
        async with session.get(url) as response:
            html = await response.text()
            soup = BeautifulSoup(html, "html.parser")
            number_tag = soup.find("p", id="number")
            if number_tag:
                return int(number_tag.text.strip())
            return 0


async def main():
    with open("problem_pages.txt", "r") as file:
        pages = file.read().splitlines()

    urls = [f"{BASE_URL}{page}.html" for page in pages]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_number(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

        total_sum = sum(results)
        print(f"Общая сумма чисел со всех страниц: {total_sum}")


asyncio.run(main())
