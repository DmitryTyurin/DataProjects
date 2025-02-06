# Ваша задача (почти та же что и в 4 степе) — дописать корутину main(), которая создаст задачу для корутины coroutine() и запланирует её выполнение. Корутина main() должна обработать исключение и напечатать сообщение об ошибке, сгенерированное в coroutine().
# raise ValueError('Секретный код')
# Корутина coroutine() скрыта "под капотом" с ней можно работать из  main().
# coroutine() выполняет только одно действие, возбуждает исключение c сообщением об ошибке (в котором хранится секретный код).


import asyncio


async def main() -> None:
    task = asyncio.create_task(coroutine())

    try:
        await task

        secret_code = task.result()
        print(secret_code)

    except Exception as e:
        print(e)


asyncio.run(main())
