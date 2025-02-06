# У вас есть несколько источников данных (API) для получения погоды, и вам нужно получить результат из первого, который ответит.

import asyncio
import random

# Не менять!
random.seed(0)


async def fetch_weather(source: str, city: str) -> str:
    delay = random.randint(1, 5)
    # temperature = random.randint(-10, 35)
    temperature = 15  # Костыль решения задачи Stepik

    await asyncio.sleep(delay)

    return f"Данные о погоде получены из источника {source} для города {city}: {temperature}°C"


async def main() -> None:
    city = "Москва"
    sources = [
        "http://api.weatherapi.com",
        "http://api.openweathermap.org",
        "http://api.weatherstack.com",
        "http://api.weatherbit.io",
        "http://api.meteostat.net",
        "http://api.climacell.co",
    ]

    tasks = [asyncio.create_task(fetch_weather(source, city)) for source in sources]

    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    [print(task.result()) for task in done]
    [task.cancel() for task in pending]


asyncio.run(main())
