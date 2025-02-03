# Ваша задача - написать асинхронный код, который позволит всем ученикам одновременно попытаться скастовать все заклинания из списка.
# Используйте asyncio.wait_for() для ограничения времени каста и asyncio.shield() для гарантии успешного завершения заклинания в качестве помощи учителя.
# Убедитесь, что ваш код корректно обрабатывает исключения и выводит соответствующие сообщения о результате каждой попытки каста.

import asyncio

# Максимальное время для каста заклинания
max_cast_time = 5  # Секунды

# Ученики мага
students = ["Алара", "Бренн", "Сирил", "Дариа", "Элвин"]

# Словарь заклинаний со временем каста
# Полный словарь заклинаний вшит в задачу
spells = {"Огненный шар": 3, "Телепортация": 7}


async def cast_spell(student: str, spell: str, cast_time: int) -> None:
    await asyncio.sleep(cast_time)

    if cast_time >= max_cast_time:
        print(
            f"Ученик {student} не справился с заклинанием {spell}, и учитель применил щит. {student} успешно завершает заклинание с помощью shield."
        )
    else:
        print(f"{student} успешно кастует {spell} за {cast_time} сек.")


async def main() -> None:

    tasks = [
        asyncio.create_task(cast_spell(student, spell, cast_time))
        for student in students
        for spell, cast_time in spells.items()
    ]
    gather = asyncio.gather(*tasks)

    try:
        await asyncio.wait_for(asyncio.shield(gather), timeout=max_cast_time)
    except asyncio.TimeoutError:
        await gather


asyncio.run(main())
