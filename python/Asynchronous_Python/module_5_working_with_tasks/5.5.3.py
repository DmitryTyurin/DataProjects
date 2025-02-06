# Напишите простой код, в котором корутина process_task() будет спать 1 секунду и возвращать id текущей задачи.
# В корутине main() запустите 10 задач. Корутина main() должна возвращать список, содержащий 10 id завершенных задач.
# Выводить на экран ничего не нужно.

import asyncio


async def process_task() -> int:
    await asyncio.sleep(1)

    current_task = asyncio.current_task()

    return id(current_task)


async def main() -> None:
    tasks = [asyncio.create_task(process_task()) for _ in range(10)]

    result = await asyncio.gather(*tasks)
    return result


asyncio.run(main())
