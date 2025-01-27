# Создайте корутину generate(), которая принимает число в качестве аргумента, имитирует время ожидания I/O-bound операции
# (используйте await asyncio.sleep(0.1)) и затем выводит сообщение в формате:
# "Корутина generate с аргументом {число}"
# Создайте корутину main(). Внутри этой корутины:
# Сгенерируйте последовательность чисел от 0 до 9 (включительно).
# Передайте каждое из этих чисел в корутину generate().
# Выполните все корутины.
# Используйте функцию asyncio.run(), чтобы запустить корутину main().

import asyncio
import time


async def generate(num: int) -> None:
    await asyncio.sleep(0.3)

    print(f"Корутина generate с аргументом {num}")


async def main() -> None:
    for i in range(10):
        await generate(i)


asyncio.run(main())
