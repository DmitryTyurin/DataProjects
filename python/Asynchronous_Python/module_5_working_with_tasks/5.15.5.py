# Напишите программу для имитации выполнения асинхронных сетевых запросов с помощью asyncio.sleep().
# Программа должна просканировать все порты на указанном маршрутизаторе в заданном диапазоне портов.
# В качестве имитации вариантов открытого или закрытого порта используйте модуль random который с вероятностью 50% решал бы, закрыт порт или открыт.

import asyncio
import random

HOST = "192.168.0.1"
MIN_PORT = 80
MAX_PORT = 85


async def scan_port(address: str, port: int) -> None | int:
    await asyncio.sleep(1)

    if random.random() < 0.5:
        print(f"Порт {port} на адресе {address} открыт")

        return port

    return None


async def scan_range(*args) -> None:
    address, start_port, end_port = args

    print(f"Сканирование портов с {start_port} по {end_port} на адресе {address}")

    try:
        async with asyncio.TaskGroup() as tg:
            tasks = [
                tg.create_task(scan_port(address, port))
                for port in range(start_port, end_port + 1)
            ]

        open_ports = [task.result() for task in tasks if task.result() is not None]

        if open_ports:
            print(f"Открытые порты на адресе {address}: {open_ports}")
        else:
            print(f"Открытых портов на адресе {address} не найдено")

    except* Exception as e:
        [print(error) for error in e.exceptions]


asyncio.run(scan_range(HOST, MIN_PORT, MAX_PORT))
