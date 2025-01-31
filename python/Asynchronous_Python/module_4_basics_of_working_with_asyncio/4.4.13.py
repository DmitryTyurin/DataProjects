# Вам предоставлен список из 10 статусов, который включает в себя состояния от "Отлично" до "Катастрофически".
# Этот список будет использоваться для имитации проверки состояния каждого компонента системы.
# Напишите три корутины (monitor_cpu(), monitor_memory(), monitor_disk_space()), каждая из которых отвечает за мониторинг определенного компонента системы.
# Каждая корутина должна проходить через список статусов, имитируя процесс проверки состояния компонента.
# Время затраченное на проверку имитируйте с помощью

import asyncio

STATUS_LIST = [
    "Отлично",
    "Хорошо",
    "Удовлетворительно",
    "Средне",
    "Пониженное",
    "Ниже среднего",
    "Плохо",
    "Очень плохо",
    "Критично",
    "Катастрофически",
]

PROCESS_LIST = ["CPU", "Память", "Дисковое пространство"]


async def monitor(status_list: list) -> None:
    task = asyncio.current_task()
    task_name = task.get_name()

    for status in status_list:
        if status == "Катастрофически":
            print(f"[{task_name}] Статус проверки: {status}")
            print(
                f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка..."
            )
        else:
            print(f"[{task_name}] Статус проверки: {status}")
        await asyncio.sleep(1)


async def main() -> None:
    tasks = [
        asyncio.create_task(monitor(STATUS_LIST), name=name) for name in PROCESS_LIST
    ]
    await asyncio.gather(*tasks)


asyncio.run(main())
