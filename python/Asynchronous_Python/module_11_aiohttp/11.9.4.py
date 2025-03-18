import aiohttp
import asyncio
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class AsyncWebScraper:
    def __init__(self, base_url, max_concurrent_requests=75):
        self.base_url = base_url
        self.max_concurrent_requests = max_concurrent_requests
        self.semaphore = asyncio.Semaphore(max_concurrent_requests)

    async def fetch_number(self, session, url):
        async with self.semaphore:
            async with session.get(url) as response:
                html = await response.text()
                soup = BeautifulSoup(html, "html.parser")
                number_tag = soup.find("p", id="number")
                if number_tag:
                    return int(number_tag.text.strip())
                return 0

    async def fetch_links(self, session, url):
        async with self.semaphore:
            async with session.get(url) as response:
                html = await response.text()
                soup = BeautifulSoup(html, "html.parser")
                links = soup.find_all("a", class_="link")
                return [urljoin(url, link["href"]) for link in links]

    async def scrape_page(self, session, url, depth):
        if depth == 2:
            return await self.fetch_number(session, url)
        else:
            links = await self.fetch_links(session, url)
            tasks = [self.scrape_page(session, link, depth + 1) for link in links]
            results = await asyncio.gather(*tasks)
            return sum(results)

    async def run(self):
        async with aiohttp.ClientSession() as session:
            total_sum = await self.scrape_page(session, self.base_url, 0)
            print(f"Общая сумма чисел со всех страниц: {total_sum}")


BASE_URL = "https://asyncio.ru/zadachi/3/index.html"
MAX_CONCURRENT_REQUESTS = 10


async def main():
    scraper = AsyncWebScraper(BASE_URL, MAX_CONCURRENT_REQUESTS)
    await scraper.run()


asyncio.run(main())
