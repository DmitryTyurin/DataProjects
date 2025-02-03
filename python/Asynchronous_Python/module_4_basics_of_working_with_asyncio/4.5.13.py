# Допишите корутину main(), так чтобы она возвращала список результатов всех задач, которые в исходном списке awaitables находятся в виде объектов корутин.
# Запускать корутину main() не нужно.
# Выводить на экран также ничего не нужно.

import asyncio


async def main():
    awaitables = [aw for aw in await get_coros_and_tasks()]
    tasks = [asyncio.ensure_future(aw) for aw in awaitables if asyncio.iscoroutine(aw)]
    results = await asyncio.gather(*tasks)
    return results
