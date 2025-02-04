# Создайте корутину upload_article(article), которая будет загружать статьи в электронную библиотеку. Корутина должна "спать" количество секунд равное длине статьи. Для контроля процесса для каждой статьи в словаре articles после загрузки добавьте ключ 'loop', а в качестве значения для этого ключа укажите ссылку на текущий объект цикла событий для каждой из статей. Вы можете использовать любой метод для получения ссылки на текущий цикл событий, но рекомендуем использовать более современный вариант.
# В корутине main() запустите задачи для загрузки каждой статьи на сервер.
# Ни одна из корутин не должна выполнять вывод на экран.
# В результате список articles после окончания работы всех задач должен быть таким:
# articles = [
#     {'title': 'Методы картирования генома', 'length': 3.2, 'loop': <ProactorEventLoop ...>},
#     ...
# ]

import asyncio

articles = [
    {"title": "Методы картирования генома", "length": 3.2},
    {"title": "Гормоны растений и их рост", "length": 4.5},
    {"title": "Применение CRISPR", "length": 2.1},
    {"title": "Микробное разнообразие", "length": 1.5},
    {"title": "Механика деления клеток", "length": 4.1},
    {"title": "Эпигенетическая регуляция", "length": 3.8},
    {"title": "Динамика сворачивания белков", "length": 4.0},
    {"title": "Экологические взаимодействия", "length": 0.7},
    {"title": "Модели нейронных сетей", "length": 4.3},
    {"title": "Пути биолюминесценции", "length": 2.9},
]


async def upload_article(article: dict) -> None:
    length = article.get("length")
    await asyncio.sleep(length)

    loop = asyncio.get_running_loop()
    article.update({"loop": loop})


async def main() -> None:
    tasks = [asyncio.create_task(upload_article(article)) for article in articles]

    await asyncio.gather(*tasks)


asyncio.run(main())
