# Ваша задача - написать асинхронный код на Python, который будет управлять процессом активации, телепортации, подзарядки, проверки стабильности, восстановления и закрытия портала.
# Каждая из этих операций требует разное количество времени, которое обозначено в единицах.
# Ваш код должен корректно выполнять все эти операции и отображать статус каждой операции в реальном времени.


import asyncio


async def activate_portal(x):
    print(f"Активация портала в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    energy = x * 2
    return energy


async def perform_teleportation(x):
    print(f"Телепортация в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    result = x + 2
    return result


async def recharge_portal(x):
    print(f"Подзарядка портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    result = x * 3
    return result


async def check_portal_stability(x):
    print(f"Проверка стабильности портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    result = x + 4
    return result


async def restore_portal(x):
    print(f"Восстановление портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    result = x * 5
    return result


async def close_portal(x):
    print(f"Закрытие портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    result = x - 1
    return result


async def portal_operator():
    activation_energy = await activate_portal(2)

    teleportation_result, recharge_result, stability_result, restore_result = (
        await asyncio.gather(
            perform_teleportation(3),
            recharge_portal(4),
            check_portal_stability(5),
            restore_portal(6),
        )
    )

    close_result = await close_portal(7)

    print(f"Результат активации портала: {activation_energy} единиц энергии")
    print(f"Результат телепортации: {teleportation_result} единиц времени")
    print(f"Результат подзарядки портала: {recharge_result} единиц энергии")
    print(f"Результат проверки стабильности портала: {stability_result} единиц времени")
    print(f"Результат восстановления портала: {restore_result} единиц энергии")
    print(f"Результат закрытия портала: {close_result} единиц времени")


asyncio.run(portal_operator())
