# В коде пропущено ключевое слово await, которое необходимо для ожидания асинхронных операций.
# Вам нужно найти место, где его отсутствие мешает правильной работе программы.


import asyncio


async def compute_square(x):
    print(f"Вычисляем квадрат числа: {x}")
    await asyncio.sleep(1)  # Имитация длительной операции
    return x * x


async def main():
    # Создаём и запускаем задачи
    tasks = [asyncio.create_task(compute_square(i)) for i in range(10)]
    # Ожидаем завершения всех задач и собираем результаты
    results = await asyncio.gather(*tasks)

    for result in results:
        print(f"Результат: {result}")


asyncio.run(main())
