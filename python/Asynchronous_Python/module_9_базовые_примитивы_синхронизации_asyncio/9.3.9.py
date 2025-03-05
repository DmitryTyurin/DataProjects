# Ваша задача: Написать код, который имитирует работу системы безопасности.
# Эта система включает в себя несколько датчиков движения (5), каждый из которых имеет уникальный идентификатор и IP-адрес.
# Датчики постоянно мониторят окружающую среду (ждут события event()), и как только обнаруживается движение,
# они активируются и выводят соответствующее сообщение.

import asyncio

ip = ["192.168.0.3", "192.168.0.1", "192.168.0.2", "192.168.0.4", "192.168.0.5"]


async def sensor(index: int, host: str, event: asyncio.Event) -> None:
    print(f"Датчик {index} IP-адрес {host} настроен и ожидает срабатывания")

    await event.wait()
    print(f'Датчик {index} IP-адрес {host} активирован, "Wee-wee-wee-wee"')


async def alarm(event: asyncio.Event) -> None:
    await asyncio.sleep(5)
    print("Датчики зафиксировали движение")

    event.set()


async def main():
    event = asyncio.Event()
    sensor_tasks = [
        asyncio.create_task(sensor(i, host, event)) for i, host in enumerate(ip)
    ]
    alarm_task = asyncio.create_task(alarm(event))

    await asyncio.gather(alarm_task, *sensor_tasks)


asyncio.run(main())
