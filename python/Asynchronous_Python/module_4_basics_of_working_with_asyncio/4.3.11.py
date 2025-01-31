# Вам необходимо исправить код ниже, который выводит сообщения от шести корутин (coroutine_1 до coroutine_6).
#
# Сначала выводятся первые сообщения от всех корутин по порядку, от первой до шестой.
# Затем выводятся вторые сообщения от всех корутин по порядку, также от первой до шестой.


import asyncio


async def coroutine_1():
    await asyncio.sleep(1.1)  # Задержка для первого сообщения
    print("Сообщение 1 от корутины 1")
    await asyncio.sleep(1.7)  # Задержка для второго сообщения
    print("Сообщение 2 от корутины 1")


async def coroutine_2():
    await asyncio.sleep(1.2)
    print("Сообщение 1 от корутины 2")
    await asyncio.sleep(1.8)
    print("Сообщение 2 от корутины 2")


async def coroutine_3():
    await asyncio.sleep(1.3)
    print("Сообщение 1 от корутины 3")
    await asyncio.sleep(1.9)
    print("Сообщение 2 от корутины 3")


async def coroutine_4():
    await asyncio.sleep(1.4)
    print("Сообщение 1 от корутины 4")
    await asyncio.sleep(2.0)
    print("Сообщение 2 от корутины 4")


async def coroutine_5():
    await asyncio.sleep(1.5)
    print("Сообщение 1 от корутины 5")
    await asyncio.sleep(2.1)
    print("Сообщение 2 от корутины 5")


async def coroutine_6():
    await asyncio.sleep(1.6)
    print("Сообщение 1 от корутины 6")
    await asyncio.sleep(2.2)
    print("Сообщение 2 от корутины 6")


async def main():
    await asyncio.gather(
        coroutine_1(),
        coroutine_2(),
        coroutine_3(),
        coroutine_4(),
        coroutine_5(),
        coroutine_6(),
    )


asyncio.run(main())
