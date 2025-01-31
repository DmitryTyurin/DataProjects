# Задача: Напишите асинхронный код, который имитирует обработку логов событий сервера.
# Каждое событие имеет свою уникальную задержку обработки (на ответ сервера).

import asyncio

log_events = [
    {"event": "Запрос на вход", "delay": 0.5},
    {"event": "Запрос данных пользователя", "delay": 1.0},
    {"event": "Обновление данных пользователя", "delay": 1.5},
    {"event": "Обновление конфигурации сервера", "delay": 5.0},
]


async def fetch_log(event: dict) -> None:
    event_name = event.get("event")
    delay = event.get("delay")

    await asyncio.sleep(delay)

    print(f"Событие: '{event_name}' обработано с задержкой {delay} сек.")


async def main() -> None:
    tasks = [asyncio.create_task(fetch_log(event)) for event in log_events]
    await asyncio.gather(*tasks)


asyncio.run(main())
