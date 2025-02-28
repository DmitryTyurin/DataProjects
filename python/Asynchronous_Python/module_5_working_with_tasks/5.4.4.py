# Ваша задача — дописать корутину main(), которая создаст задачу для корутины coroutine() и запланирует её выполнение. Корутина main() должна дождаться результата от корутины coroutine() и напечатать его, когда результат станет доступен.
# Корутина coroutine() скрыта "под капотом", к ней можно обратиться за результатом из функции main().
# coroutine() выполняет только два действия: засыпает на случайное время (от 1 до 6 секунд) и после этого возвращает секретный код, который нужен для решения задачи.

import asyncio


async def main() -> None:
    task = asyncio.create_task(coroutine())
    await task

    secret_code = task.result()
    print(secret_code)


asyncio.run(main())
