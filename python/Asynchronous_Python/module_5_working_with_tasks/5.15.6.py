# Написать асинхронный код для сканирования заданного диапазона портов определенных IP-адресов, с целью определить, какие из этих портов являются открытыми.

import asyncio
import random

IP_DICT = {
    "192.168.0.1": [0, 100],
    "192.168.0.2": [225, 300],
    "192.168.2.5": [150, 185],
}


async def scan_port(address: str, port: int) -> int | None:
    await asyncio.sleep(1)

    if random.randint(0, 100) == 1:
        print(f"Port {port} on {address} is open")

        return port

    return None


async def scan_range(*args) -> tuple[str, list[int]]:
    address, start_port, end_port = args

    print(f"Scanning ports {start_port}-{end_port} on {address}")

    try:
        async with asyncio.TaskGroup() as tg:
            tasks = [
                tg.create_task(scan_port(address, port))
                for port in range(start_port, end_port + 1)
            ]

        open_ports = sorted(
            [task.result() for task in tasks if task.result() is not None]
        )

        return address, open_ports

    except* Exception as e:
        [print(error) for error in e.exceptions]


async def main(ip_dict: dict[str, list[int]]) -> None:
    try:
        async with asyncio.TaskGroup() as tg:
            tasks = [
                tg.create_task(scan_range(address, ports[0], ports[1]))
                for address, ports in ip_dict.items()
            ]

        open_ports = sorted(
            [task.result() for task in tasks if task.result() is not None]
        )

        [
            print(
                f"Всего найдено открытых портов {len(ports)} {ports} для ip: {address}"
            )
            for address, ports in open_ports
            if len(ports) > 0
        ]

    except* Exception as e:
        [print(error) for error in e.exceptions]


asyncio.run(main(IP_DICT))
