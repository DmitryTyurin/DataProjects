# Ваша задача — написать асинхронный код для получения кода со страницы и его расшифровки.
# Ваш код должен сделать всего 1 асинхронный запрос на указанный адрес.

import aiohttp
import asyncio
from bs4 import BeautifulSoup

url = "https://asyncio.ru/zadachi/1/index.html"

code_dict = {
    0: "F",
    1: "B",
    2: "D",
    3: "J",
    4: "E",
    5: "C",
    6: "H",
    7: "G",
    8: "A",
    9: "I",
}


async def fetch_and_decode(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            page_content = await response.text()

            soup = BeautifulSoup(page_content, "html.parser")
            p_text = soup.find("p").text.strip()

            decoded_text = "".join([code_dict[int(digit)] for digit in p_text])

            return decoded_text


async def main():
    decoded_message = await fetch_and_decode(url)
    print(decoded_message)


asyncio.run(main())
