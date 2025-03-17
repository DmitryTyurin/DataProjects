# Ваша задача — написать асинхронный скрипт на Python, который будет сканировать веб-страницы, собирать их статус-коды и суммировать их.

import aiohttp
import asyncio
import logging

SEMAPHORE_COUNT = 10


class ScannerStatusCodes:
    def __init__(self, semaphore_count: int = 10):
        self.status_codes = []
        self.semaphore_count = semaphore_count

    async def get_status_code(
        self, session: aiohttp.ClientSession, url: str, semaphore: asyncio.Semaphore
    ) -> int:
        async with semaphore:
            try:
                async with session.get(url) as response:
                    status_code = response.status
                    self.status_codes.append(status_code)
                    return status_code
            except aiohttp.ClientError as e:
                logging.warning(e)

    async def scan_urls(self):
        semaphore = asyncio.Semaphore(self.semaphore_count)
        try:
            async with aiohttp.ClientSession() as session:
                async with asyncio.TaskGroup() as tg:
                    [
                        tg.create_task(
                            self.get_status_code(
                                session,
                                f"https://asyncio.ru/zadachi/5/{i}.html",
                                semaphore,
                            )
                        )
                        for i in range(1, 1001)
                    ]
        except* Exception as e:
            [logging.warning(error) for error in e.exceptions]

    async def sum_status_codes(self):
        logging.warning(sum(self.status_codes))


scan = ScannerStatusCodes(SEMAPHORE_COUNT)
asyncio.run(scan.scan_urls())
asyncio.run(scan.sum_status_codes())
