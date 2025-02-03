# Ваш скрипт должен асинхронно проверить каждую книгу на наличие на полке и вывести информацию о всех отсутствующих книгах, включая их порядковый номер,
# автора, название и год издания. Формат вывода должен соответствовать следующему примеру:
# Примените asyncio.gather() для запуска и сбора результатов проверки каждой книги.
# Отфильтруйте и выведите результаты, показывающие только те книги, которые отсутствуют на полке.
# Операция поиска является асинхронной и для одной книги занимает 0.1 секунды.
# Имитируйте ожидание ее завершения при помощи await asyncio.sleep(.1)

import asyncio

books_json = [
    {
        "Порядковый номер": 1,
        "Автор": "Rebecca Butler",
        "Название": "Three point south wear score organization.",
        "Год издания": "1985",
        "Наличие на полке": False,
    },
    {
        "Порядковый номер": 2,
        "Автор": "Mark Cole",
        "Название": "Drive experience customer somebody pressure.",
        "Год издания": "1985",
        "Наличие на полке": True,
    },
]


async def check_book(book: dict) -> None:
    await asyncio.sleep(0.1)
    if not book["Наличие на полке"]:
        print(
            f'{book["Порядковый номер"]}: {book["Автор"]}: {book["Название"]} ({book["Год издания"]})'
        )


async def main() -> None:
    tasks = [asyncio.create_task(check_book(book)) for book in books_json]
    await asyncio.gather(*tasks)


asyncio.run(main())
