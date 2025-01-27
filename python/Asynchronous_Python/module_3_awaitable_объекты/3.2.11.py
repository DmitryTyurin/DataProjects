# Создайте асинхронную функцию (корутину) с именем main(), которая при вызове выводит на экран сообщение:
# Hello, Asyncio!
# Используйте функцию asyncio.run(), чтобы запустить вашу корутину.
# Не забудьте об импорте необходимой библиотеки.

import asyncio
import time


async def main() -> None:
    print("Hello, Asyncio!")


asyncio.run(main())
