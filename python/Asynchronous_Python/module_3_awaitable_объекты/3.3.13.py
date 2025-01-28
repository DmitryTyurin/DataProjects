# Для решения этой задачи вам потребуется усовершенствовать предыдущую задачу, добавив ещё один счётчик, и определить свое время задержки для каждого счетчика.
# В этой версии добавьте еще один счетчик - "Counter 3". Мы также добавили словарь delays, который определяет время задержки для каждого счетчика. Таким образом, каждый счетчик "тикает" с разной скоростью.
# Словарь max_counts хранит максимальное значение, на которое каждый счетчик должен быть инкрементирован.

import asyncio

counters = {"Counter 1": 0, "Counter 2": 0, "Counter 3": 0}
max_counts = {"Counter 1": 10, "Counter 2": 5, "Counter 3": 15}
delays = {"Counter 1": 1, "Counter 2": 2, "Counter 3": 0.5}


async def counter(name: str) -> None:
    while counters[name] < max_counts[name]:
        counters[name] += 1
        await asyncio.sleep(delays[name])
        print(f"{name}: {counters[name]}")


async def main() -> None:
    tasks = [asyncio.create_task(counter(i)) for i in counters]

    await asyncio.gather(*tasks)


asyncio.run(main())
