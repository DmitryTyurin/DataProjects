# Дописать функцию reserve_book(), так чтобы она проверяла наличие книги в библиотеке, а далее ожидала 1 секунду, прежде чем выполнить следующие действия:
# В случае успешной проверки через секунду корутина должна изменять количество оставшихся в наличии книг и выводить на экран сообщение:

import asyncio

# Библиотечный каталог
library_catalog = {
    "Мастер и Маргарита": 3,
    "Война и мир": 2,
    "Преступление и наказание": 1,
}

# Резервирование книг для пользователей
reservation_tasks = {
    "Алексей": "Мастер и Маргарита",
    "Ирина": "Мастер и Маргарита",
    "Сергей": "Война и мир",
    "Елена": "Преступление и наказание",
    "Анна": "Мастер и Маргарита",
    "Игорь": "Война и мир",
    "Мария": "Преступление и наказание",
}


async def reserve_book(book: str) -> None:
    if book in library_catalog and library_catalog[book] > 0:
        await asyncio.sleep(1)
        library_catalog[book] -= 1
        print("Книга успешно зарезервирована.")
    else:
        print("Книга отсутствует. Резервирование отменено.")


async def main() -> None:
    try:
        async with asyncio.TaskGroup() as tg:
            [
                tg.create_task(reserve_book(book))
                for user, book in reservation_tasks.items()
            ]

    except* Exception as e:
        [print(error) for error in e.exceptions]

    [print(f"{book}: {count}") for book, count in library_catalog.items()]


asyncio.run(main())
