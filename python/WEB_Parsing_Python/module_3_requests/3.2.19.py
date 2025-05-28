# Перейдите на сайт
# Скачайте видео с сайта  при помощи requests
# Определите его размер вручную
# Напишите размер файла в поле для ответа. Написать нужно только число в мегабайтах.

import requests

url = "https://parsinger.ru/video_downloads/videoplayback.mp4"

try:
    response = requests.get(url, stream=True)
    response.raise_for_status()

    file_size_bytes = int(response.headers.get("content-length", 0))
    file_size_mb = round(file_size_bytes / (1024 * 1024), 2)

    print(file_size_mb)

except requests.exceptions.RequestException as e:
    print(f"Ошибка при скачивании файла: {e}")
