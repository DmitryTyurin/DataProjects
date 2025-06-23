# Откройте сайт тренажёр;
# Напишите асинхронный код, который обработает все карточки(160шт);
# Необходимо вычислить общий размер скидки для всех товаров в рублях


import aiohttp
import asyncio
from bs4 import BeautifulSoup
import re
import time


class DataDriver:
    def __init__(self):
        self.base_url = "https://parsinger.ru/html/"
        self.pagen_urls = []
        self.product_urls = []
        self.total_discount = 0
        self.session = None

    @staticmethod
    def extract_digits(text: str) -> int:
        digits = re.findall(r"\d+", text)
        return int("".join(digits)) if digits else 0

    async def fetch(self, session: aiohttp.ClientSession, url: str) -> str:
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                return await response.text(encoding="utf-8")
        except Exception as e:
            print(f"Ошибка при запросе {url}: {e}")
            return ""

    async def get_pagen_urls(self, session: aiohttp.ClientSession):
        tasks = []
        for i in range(1, 6):
            url = f"{self.base_url}index{i}_page_1.html"
            tasks.append(self.fetch(session, url))

        pages_html = await asyncio.gather(*tasks)

        for html in pages_html:
            if not html:
                continue
            soup = BeautifulSoup(html, "lxml")
            pagen_div = soup.find("div", class_="pagen")
            if pagen_div:
                self.pagen_urls.extend(
                    f"{self.base_url}{a['href']}" for a in pagen_div.find_all("a")
                )

    async def get_product_urls(self, session: aiohttp.ClientSession):
        if not self.pagen_urls:
            return

        tasks = []
        for url in self.pagen_urls:
            tasks.append(self.fetch(session, url))

        pages_html = await asyncio.gather(*tasks)

        for html in pages_html:
            if not html:
                continue
            soup = BeautifulSoup(html, "lxml")
            product_links = soup.find_all("a", class_="name_item")
            self.product_urls.extend(
                f"{self.base_url}{link['href']}" for link in product_links
            )

    async def process_product(self, session: aiohttp.ClientSession, url: str):
        html = await self.fetch(session, url)
        if not html:
            return 0

        soup = BeautifulSoup(html, "lxml")

        stock = self.extract_digits(soup.find(id="in_stock").text)
        price = self.extract_digits(soup.find(id="price").text)
        old_price = self.extract_digits(soup.find(id="old_price").text)

        return (old_price - price) * stock

    async def calculate_total_discount(self):
        async with aiohttp.ClientSession() as session:
            await self.get_pagen_urls(session)
            await self.get_product_urls(session)

            tasks = [self.process_product(session, url) for url in self.product_urls]

            for task in asyncio.as_completed(tasks):
                result = await task
                self.total_discount += result

    async def run_data_driver(self):
        await self.calculate_total_discount()

        print(self.total_discount)


def main():
    import time

    start_time = time.perf_counter()

    d = DataDriver()
    asyncio.run(d.run_data_driver())

    end_time = time.perf_counter()

    print(f"Время выполнения: {end_time - start_time:.2f} секунд")


main()
