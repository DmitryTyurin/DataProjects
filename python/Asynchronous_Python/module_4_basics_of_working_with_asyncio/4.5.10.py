# Ваша задача состоит в том, чтобы написать асинхронный код, который будет имитировать процесс активации портала и последующую телепортацию.
# Каждая операция требует определенного времени и выделяет или использует определенное количество единиц энергии.

import asyncio


async def activate_portal(x):
    print(f"Активация портала в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x * 2


async def perform_teleportation(x):
    print(f"Телепортация в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x + 2


async def portal_operator():
    activation_result = await activate_portal(2)
    if activation_result > 4:
        teleportation_time = 1
    else:
        teleportation_time = activation_result
    teleportation_result = await perform_teleportation(teleportation_time)
    print(f"Результат активации портала: {activation_result} единиц энергии")
    print(f"Результат телепортации: {teleportation_result} единиц времени")


asyncio.run(portal_operator())
