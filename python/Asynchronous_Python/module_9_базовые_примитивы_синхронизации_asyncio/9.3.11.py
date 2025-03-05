# Ваша задача: ознакомьтесь с описанием функций и напишите две функции — monitor_rocket_launches() и main().
# Подумайте, как в данном коде применить прерывания (interrupts) с помощью флага asyncio.Event() и методов .set(), .is_set(), .clear() для прерывания запущенной в функции main() Task задачи.

import asyncio
import random

error = None
count = 0
sek = 0


async def monitor_rocket_launches(interrupt_flag: asyncio.Event) -> None:
    global count
    global error
    global sek
    try:
        while not error:
            if random.random() < 0.25:
                error = True
            print(
                f"Мониторинг ракетных запусков... (Запуск номер {count} прошёл успешно)"
            )
            count += 1
            await asyncio.sleep(1)
    finally:
        print("Завершение мониторинга ракетных запусков")


async def main() -> None:
    global error
    global count
    global sek
    interrupt_flag = asyncio.Event()
    task = asyncio.create_task(monitor_rocket_launches(interrupt_flag))

    while True:
        await asyncio.sleep(5)
        sek += 5
        if count == 50 or error:
            if error:
                print(f"Ошибка при запуске произошла на {sek} секунде =(")
                print("Отмена мониторинга ракетных запусков...")
            break
        else:
            print(
                f"Время ожидания составило {sek} секунд. За это время ошибки не произошло"
            )

    await task


asyncio.run(main())
