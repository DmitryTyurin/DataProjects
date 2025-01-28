# Создайте три корутины, которые будут выводить следующие сообщения:
#
# Coroutine 1 is done
# Coroutine 2 is done
# Coroutine 3 is done
# Используя библиотеку asyncio, создайте три задачи для ранее созданных корутин.
#
# Запустите все задачи одновременно, используя asyncio.run().

import asyncio


async def coroutine(num: int) -> None:
    print(f"Coroutine {num} is done")


async def main() -> None:
    tasks = [asyncio.create_task(coroutine(i)) for i in range(1, 4)]

    await asyncio.gather(*tasks)


asyncio.run(main())
