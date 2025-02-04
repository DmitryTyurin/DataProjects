# Предлагаем вам создать и запустить корутину main() не через высокоуровневый asyncio.run(), а с помощью метода loop.run_until_complete().

import asyncio


async def main():
    print("Корутина завершена")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
