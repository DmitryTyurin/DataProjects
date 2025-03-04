# Напишите асинхронный код, который управляет процессом посадки самолетов с использованием приоритетной очереди.
# Сценарий представляет ситуацию в аэропорту, где каждый рейс имеет определенный приоритет в зависимости от факторов, таких как срочность, погодные условия и расписание.

import asyncio

flights = [
    ("Delta Air Lines DL758", 1.0),
    ("United Airlines UA1189", 2.1),
    ("Southwest Airlines WN3920", 1.2),
    ("American Airlines AA2401", 2.7),
    ("Spirit Airlines NK301", 3.1),
    ("Alaska Airlines AS621", 1.4),
    ("JetBlue Airways B61883", 1.8),
    ("Frontier Airlines F91514", 3.0),
    ("Hawaiian Airlines HA22", 2.4),
    ("Allegiant Air G4159", 1.1),
    ("Air Canada AC758", 2.9),
    ("Lufthansa LH447", 3.3),
    ("British Airways BA183", 2.3),
    ("Qantas QF12", 1.3),
    ("Emirates EK231", 1.5),
]


async def process_flights(queue):
    while not queue.empty():
        await asyncio.sleep(1)

        priority, flight = await queue.get()
        print(f"Посадка самолёта: {flight} с приоритетом {priority}")

        queue.task_done()


async def main():
    queue = asyncio.PriorityQueue()

    [await queue.put((priority, flight)) for flight, priority in flights]

    await process_flights(queue)
    await queue.join()


asyncio.run(main())
