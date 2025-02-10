# На вход будет подаваться количество дней до нового года и список заказов, которые нужно отправить. Входящие данные будут автоматически преобразованы в переменные следующего вида:
# Количество дней до нового года доступно через переменную days_left.
# Список заказов - это список кортежей следующего формата (каждый кортеж - это заказ):
# orders = [(подарок, город, пометка), ...].
# Внимание! Вам не нужно реализовывать input() и ничего не нужно вводить с консоли!
# В своем решении просто обращайтесь к days_left и orders, они будут сформированы автоматически!
# Для каждого заказа надо оформить доставку. Все заказы должны быть одновременно отправлены, но те заказы, которые не успеют прийти до нового года, должны быть отменены.
# Исключение составляют заказы с пометкой "важно". Они должны быть доставлены вне зависимости от времени доставки, для гарантии их доставки используйте функцию shield().

import asyncio

days_left = 3
orders = [
    ("Новогодняя кружка", "Москва", "нет"),
    ("Шоколадный набор", "Красноярск", "нет"),
    ("Ручка и блокнот", "Новосибирск", "важно"),
    ("Носки с новогодним принтом", "Владивосток", "нет"),
    ("Плед", "Омск", "нет"),
]


delivery_times = {
    "Москва": 1,
    "Санкт-Петербург": 3,
    "Новосибирск": 7,
    "Екатеринбург": 5,
    "Нижний Новгород": 4,
    "Челябинск": 6,
    "Омск": 7,
    "Красноярск": 8,
    "Владивосток": 9,
    "Хабаровск": 9,
}


async def deliver(item: str, city: str) -> None:
    days = delivery_times.get(city)

    await asyncio.sleep(days)
    print(f"Подарок {item} успешно доставлен в г. {city}")


async def main(days_left: int, orders: list) -> None:
    tasks = []

    for order in orders:
        item, city, important = order

        if important == "важно":
            task = asyncio.shield(deliver(item, city))
        else:
            task = asyncio.create_task(deliver(item, city))
        tasks.append(task)

    active_tasks = asyncio.all_tasks()
    active_tasks.discard(asyncio.current_task())

    done, pending = await asyncio.wait(tasks, timeout=days_left)

    [task.cancel() for task in pending]

    for task in active_tasks:
        try:
            await task
        except asyncio.CancelledError as ex:
            pass


asyncio.run(main(days_left, orders))
