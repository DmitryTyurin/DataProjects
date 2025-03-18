# Скачать 1000 изображений с целевой веб-страницы.
# Подсчитать общий размер всех скачанных изображений.

import os
import aiohttp
import asyncio
from bs4 import BeautifulSoup
from urllib.parse import urljoin


async def download_image(session, url, folder_path):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                image_name = url.split("/")[-1]
                image_path = os.path.join(folder_path, image_name)
                with open(image_path, "wb") as f:
                    f.write(await response.read())
                print(image_name)
            else:
                print(f"{url}: {response.status}")
    except Exception as e:
        print(f"ОШИБКА: {url}: {e}")


async def fetch_image_urls(session, url):
    async with session.get(url) as response:
        html_content = await response.text()
        soup = BeautifulSoup(html_content, "html.parser")
        main_tag = soup.find("main")
        img_tags = main_tag.find_all("img")
        return [urljoin(url, img["src"]) for img in img_tags]


async def download_all_images(url, folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    async with aiohttp.ClientSession() as session:
        image_urls = await fetch_image_urls(session, url)
        tasks = [
            download_image(session, img_url, folder_path) for img_url in image_urls
        ]
        await asyncio.gather(*tasks)


def get_folder_size(folder_path):
    total_size = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
    return total_size


async def main():
    target_url = "https://asyncio.ru/zadachi/4/index.html"
    folder_path = r"downloaded_images"

    await download_all_images(target_url, folder_path)
    total_size = get_folder_size(folder_path)
    print(f"Общая сумма байт со всех страниц {total_size}")


asyncio.run(main())
