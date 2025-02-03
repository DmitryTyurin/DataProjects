# Условия задачи:
# Допишите корутину main(), так чтобы она возвращала список результатов всех задач, которые есть в исходном списке awaitables, в том же порядке.
# Запускать корутину main() не нужно.
# Выводить на экран ничего не нужно.


async def main():
    awaitables = [aw for aw in await get_coros_and_tasks()]
    tasks = [asyncio.ensure_future(aw) for aw in awaitables]
    results = await asyncio.gather(*tasks)
    return results
