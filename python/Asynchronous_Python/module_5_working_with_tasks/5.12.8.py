# Усовершенствуем предыдущую задачу, добавив в неё условие, которое проверяет, является ли код четным или нечетным
# (основываясь на последнем символе в коде), и в зависимости от этого выводит разные сообщения.


import asyncio

codes = [
    "56FF4D",
    "A3D2F7",
    "B1C94A",
    "F56A1D",
    "D4E6F1",
    "A1B2C3",
    "D4E5F6",
    "A7B8C9",
    "D0E1F2",
    "A3B4C5",
    "D6E7F8",
    "A9B0C1",
    "D2E3F4",
    "A5B6C7",
    "D8E9F2",
]
messages = [
    "Привет, мир!",
    "Как дела?",
    "Что нового?",
    "Добрый день!",
    "Пока!",
    "Спокойной ночи!",
    "Удачного дня!",
    "Всего хорошего!",
    "До встречи!",
    "Счастливого пути!",
    "Успехов в работе!",
    "Приятного аппетита!",
    "Хорошего настроения!",
    "Спасибо за помощь!",
    "Всего наилучшего!",
]


def print_code(task) -> None:
    index = task.result()
    print(f"Код: {codes[index]}")


def is_last_digit_even(hex_char: str) -> bool:
    decimal_value = int(hex_char, 16)

    return decimal_value % 2 == 0


async def print_message(index: int) -> int:
    if is_last_digit_even(codes[index][-1]):
        print("Сообщение: Неверный код, сообщение скрыто")
    else:
        print(f"Сообщение: {messages[index]}")
    return index


async def main() -> None:
    for i in range(len(codes)):
        task = asyncio.create_task(print_message(i))
        task.add_done_callback(print_code)
        await task


asyncio.run(main())
