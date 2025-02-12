# Реализовать асинхронный генератор monitor_servers(servers), который будет итерироваться по списку
# серверов из списка SERVERS, проверяя их состояние и возвращая результат в виде кортежа: (server, status).
# Проверка состояния каждого сервера должна имитировать реальный запрос, используя асинхронную задержку в 0.1 секунду.
# Для каждого сервера состояние должно выбираться случайно из списка STATUSES функцией random.choice().
# В корутине main() выполните асинхронную итерацию по объекту генератора monitor_servers(servers),
# выводя для каждого сервера данные в формате: f'{server}: состояние {status}'.

import asyncio
import random

random.seed(1)

SERVERS = [
    "api.database.local",
    "auth.backend.local",
    "web.frontend.local",
    "cache.redis.local",
    "analytics.bigdata.local",
]

STATUSES = ["Online", "Offline", "Maintenance", "Error"]


async def monitor_servers(servers):
    for server in servers:
        await asyncio.sleep(0.1)
        status = random.choice(STATUSES)

        yield (server, status)


async def main(servers) -> None:
    async for server, status in monitor_servers(servers):
        print(f"{server}: состояние {status}")


asyncio.run(main(SERVERS))
