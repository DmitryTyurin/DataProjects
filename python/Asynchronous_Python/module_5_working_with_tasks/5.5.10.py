# Допишите корутину cancel_task(task):
# Корутина должна отменять задачу, переданную в качестве аргумента.
# Корутина не должна ничего возвращать, также она не должна выводить на экран никаких сообщений.
# Допишите корутину download_data(report):
# Для пользователя "Дмитрий Орлов" задача должна отменяться сразу после старта, используйте корутину cancel_task() для отмены задачи. Используйте метод current_task() для получения ссылки на текущую задачу.
# Для других пользователей отчет должен загружаться до конца.
# После формирования отчета корутина должна отправлять сообщение: f"Отчет: {report_name} для пользователя {name} готов"
# При отмене задачи, корутина должна выводить сообщение f"Загрузка отчета {report_name} для пользователя {name} остановлена. Введите новые данные".
# Допишите корутину main():
# Запустите загрузку всех отчетов и дождитесь завершения всех задач.
# Не забудьте про обработку ошибок asyncio.CancelledError.


import asyncio

reports = [
    {"name": "Алексей Иванов", "report": "Отчет о прибылях и убытках", "load_time": 5},
    {
        "name": "Мария Петрова",
        "report": "Прогнозирование движения денежных средств",
        "load_time": 4,
    },
    {"name": "Иван Смирнов", "report": "Оценка инвестиционных рисков", "load_time": 3},
    {
        "name": "Елена Кузнецова",
        "report": "Обзор операционных расходов",
        "load_time": 2,
    },
    {"name": "Дмитрий Орлов", "report": "Анализ доходности активов", "load_time": 10},
]


async def download_data(report: dict):
    name = report.get("name")
    report_name = report.get("report")
    load_time = report.get("load_time")

    if name == "Дмитрий Орлов":
        current_task = asyncio.current_task()
        await cancel_task(current_task)

    try:
        await asyncio.sleep(load_time)
        print(f"Отчет: {report_name} для пользователя {name} готов")

    except asyncio.CancelledError:
        print(
            f"Загрузка отчета {report_name} для пользователя {name} остановлена. Введите новые данные"
        )


async def cancel_task(task) -> None:
    task.cancel()


async def main() -> None:
    tasks = [asyncio.create_task(download_data(report)) for report in reports]

    gather = asyncio.gather(*tasks)
    await gather


asyncio.run(main())
