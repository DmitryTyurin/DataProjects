# С помощью asyncio.sleep(0) настройте переключение контекста между двумя задачами таким образом, чтобы после завершения каждого этапа выводился текущий статус запроса.
# Запускать функцию main() не нужно, ее запуск происходит автоматически. Ваша задача только добавить переключение контекста в нужных местах.

import asyncio
import time


async def process_request(request_name, stages, status):
    for stage_name in stages:
        await asyncio.sleep(0)  # Симулируем время выполнения этапа
        status[request_name] = stage_name


async def update_status(request_name, status):
    while True:
        if status[request_name] is not None:  # Выводим статус только если он не None
            print(status)
        if status[request_name] == "Отправка уведомлений":
            break
        await asyncio.sleep(0)  # Переключение контекста


async def main():
    request_name = "Запрос 1"
    stages = [
        "Загрузка данных",
        "Проверка данных",
        "Анализ данных",
        "Сохранение результатов",
        "Отправка уведомлений",
    ]

    status = {request_name: None}

    process_task = asyncio.create_task(process_request(request_name, stages, status))
    updater_task = asyncio.create_task(update_status(request_name, status))

    await asyncio.gather(process_task, updater_task)


asyncio.run(main())
