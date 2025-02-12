# Реализуйте асинхронную функцию user_action_generator(), которая будет асинхронным генератором данных о действиях пользователей.
# Генератор должен непрерывно генерировать словарь, в котором значения случайным образом выбираются из списков users, products и actions:
# {'user_id': user, 'action': action, 'product_id': product}
# На экран выводить ничего не нужно. Напишите только асинхронный генератор.

import asyncio

users = ["user1", "user2", "user3"]
products = [
    "iPhone 14",
    "Samsung Galaxy S23",
    "MacBook Pro",
    "Dell XPS 13",
    "Sony WH-1000XM5",
    "Apple Watch Series 8",
    "Kindle Paperwhite",
    "GoPro Hero 11",
    "Nintendo Switch",
    "Oculus Quest 2",
]
actions = ["просмотр", "покупка", "добавление в избранное"]


async def user_action_generator():
    while True:
        user = random.choice(users)
        product = random.choice(products)
        action = random.choice(actions)

        yield {"user_id": user, "action": action, "product_id": product}
