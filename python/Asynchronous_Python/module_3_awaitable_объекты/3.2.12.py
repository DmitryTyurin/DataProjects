# Создайте две корутины: coro_1() и coro_2().
# Каждая из корутин при вызове должна выводить своё уникальное приветственное сообщение.
# Корутины должны "поприветствовать" друг друга в своих сообщениях.
# Создайте корутину main(), в которой запустите обе корутины, сначала корутину coro_1(),затем coro_2().
# Используйте функцию asyncio.run(), чтобы запустить корутину main().

import asyncio
import time


async def coro_1() -> None:
    print("coro_1 says, hello coro_2!")


async def coro_2() -> None:
    print("coro_2 says, hello coro_1!")


async def main() -> None:
    await coro_1()
    await coro_2()


asyncio.run(main())
