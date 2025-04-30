# Описание задачи:
# Разработать многопоточное приложение для проверки наличия товаров на складе и расчета общей стоимости товаров, используя данные о товарах, хранящиеся в словаре.
#
# Этапы реализации:
# Создание необходимого количества потоков:
#
# Используйте ThreadPoolExecutor для создания пула потоков. Количество потоков должно быть достаточным для обработки всех товаров, например, равным количеству товаров в словаре.
# Использование словаря с данными:
#
# Словарь products, где каждый ключ — это уникальный идентификатор товара, а значение — это словарь с информацией о товаре (название, цена, количество на складе). Словарь products вшит в задачу, вставлять его в поле ответа не нужно.
# products
# products = {
#     1: {"name": "Компьютер ProMax", "price": 50000, "stock": 5},
#     2: {"name": "Телефон UltraTalk", "price": 30000, "stock": 1},
#     3: {"name": "Наушники SoundBeats", "price": 2000, "stock": 0},
#     4: {"name": "Планшет ViewTab", "price": 15000, "stock": 20},
#     5: {"name": "Монитор ClearView", "price": 10000, "stock": 15},
#     6: {"name": "Клавиатура QuickType", "price": 1500, "stock": 30},
#     7: {"name": "Мышь Clicker", "price": 800, "stock": 40},
#     8: {"name": "Флешка SpeedDrive", "price": 500, "stock": 0},
#     9: {"name": "Жесткий диск StoreMore", "price": 4000, "stock": 25},
#     10: {"name": "Принтер PrintAll", "price": 6000, "stock": 12},
#     11: {"name": "Смартфон FlexPhone", "price": 25000, "stock": 18},
#     12: {"name": "Ноутбук CarryComp", "price": 45000, "stock": 8},
#     13: {"name": "Камера SnapShot", "price": 8000, "stock": 22},
#     14: {"name": "Проектор LightShow", "price": 12000, "stock": 0},
#     15: {"name": "Спикеры SoundWave", "price": 2500, "stock": 35},
#     16: {"name": "Монопод SelfieStick", "price": 700, "stock": 60},
#     17: {"name": "Роутер NetFast", "price": 3000, "stock": 28},
#     18: {"name": "Планшет SketchTab", "price": 13000, "stock": 0},
#     19: {"name": "Микрофон EchoMic", "price": 1500, "stock": 45},
#     20: {"name": "Веб-камера VisionPro", "price": 2000, "stock": 0},
#     21: {"name": "Наушники BassHead", "price": 1800, "stock": 55},
#     22: {"name": "Мышь для геймеров GameMaster", "price": 1200, "stock": 38},
#     23: {"name": "Клавиатура для геймеров KeyStrike", "price": 2500, "stock": 0},
#     24: {"name": "Графический планшет DrawMaster", "price": 8000, "stock": 17},
#     25: {"name": "Смарт-часы TimeTech", "price": 3000, "stock": 23},
#     26: {"name": "Компьютерные колонки SoundSpace", "price": 3500, "stock": 30},
#     27: {"name": "Беспроводная мышь FreedomClick", "price": 1000, "stock": 42},
#     28: {"name": "Смартфон Samsung GalaxyZ", "price": 27000, "stock": 0},
#     29: {"name": "Смартфон iPhone X", "price": 35000, "stock": 9},
#     30: {"name": "Ноутбук Dell Inspire", "price": 48000, "stock": 7},
# }
# Проверка товара на складе:
#
# Реализуйте функцию search_product, которая принимает идентификатор товара, проверяет его наличие и количество на складе. Если товар закончился ("stock": 0), функция должна выводить сообщение о том, что товар закончился. Если товар есть в наличии, функция должна выводить информацию о товаре.
# Поиск товара: Компьютер ProMax
#
# print(f"Поиск товара: {product_name}")
#
#
#
# Товар ID 3 закончился на складе.
#
# print(f"Товар ID {product_id} закончился на складе.")
# Отслеживание завершения задачи:
#
# После завершения каждой задачи по поиску товара, программа должна выводить сообщение о завершении поиска и статусе задачи, используя future.done() для подтверждения завершения.
# Поиск завершён, статус: True
#
# print(f'Поиск завершён, статус: {future.done()}')
# Расчет общей стоимости товаров:
#
# По мере выполнения каждой задачи, суммируйте стоимость всех товаров на складе, умножая цену товара на его количество. В конце работы программы выведите общую стоимость всех товаров на складе
# "price": 50000 * "stock": 5 = 250000.
# Общая стоимость товаров на складе: *******
#
# print(f'Общая стоимость товаров на складе: {total_cost}')

import concurrent.futures

products = {
    1: {"name": "Компьютер ProMax", "price": 50000, "stock": 5},
    2: {"name": "Телефон UltraTalk", "price": 30000, "stock": 1},
    3: {"name": "Наушники SoundBeats", "price": 2000, "stock": 0},
    4: {"name": "Планшет ViewTab", "price": 15000, "stock": 20},
    5: {"name": "Монитор ClearView", "price": 10000, "stock": 15},
    6: {"name": "Клавиатура QuickType", "price": 1500, "stock": 30},
    7: {"name": "Мышь Clicker", "price": 800, "stock": 40},
    8: {"name": "Флешка SpeedDrive", "price": 500, "stock": 0},
    9: {"name": "Жесткий диск StoreMore", "price": 4000, "stock": 25},
    10: {"name": "Принтер PrintAll", "price": 6000, "stock": 12},
    11: {"name": "Смартфон FlexPhone", "price": 25000, "stock": 18},
    12: {"name": "Ноутбук CarryComp", "price": 45000, "stock": 8},
    13: {"name": "Камера SnapShot", "price": 8000, "stock": 22},
    14: {"name": "Проектор LightShow", "price": 12000, "stock": 0},
    15: {"name": "Спикеры SoundWave", "price": 2500, "stock": 35},
    16: {"name": "Монопод SelfieStick", "price": 700, "stock": 60},
    17: {"name": "Роутер NetFast", "price": 3000, "stock": 28},
    18: {"name": "Планшет SketchTab", "price": 13000, "stock": 0},
    19: {"name": "Микрофон EchoMic", "price": 1500, "stock": 45},
    20: {"name": "Веб-камера VisionPro", "price": 2000, "stock": 0},
    21: {"name": "Наушники BassHead", "price": 1800, "stock": 55},
    22: {"name": "Мышь для геймеров GameMaster", "price": 1200, "stock": 38},
    23: {"name": "Клавиатура для геймеров KeyStrike", "price": 2500, "stock": 0},
    24: {"name": "Графический планшет DrawMaster", "price": 8000, "stock": 17},
    25: {"name": "Смарт-часы TimeTech", "price": 3000, "stock": 23},
    26: {"name": "Компьютерные колонки SoundSpace", "price": 3500, "stock": 30},
    27: {"name": "Беспроводная мышь FreedomClick", "price": 1000, "stock": 42},
    28: {"name": "Смартфон Samsung GalaxyZ", "price": 27000, "stock": 0},
    29: {"name": "Смартфон iPhone X", "price": 35000, "stock": 9},
    30: {"name": "Ноутбук Dell Inspire", "price": 48000, "stock": 7},
}


class DataProduct:
    def __init__(self, products: dict):
        self.products = products
        self.execute = concurrent.futures.ThreadPoolExecutor(
            max_workers=len(self.products)
        )
        self.total_cost = 0

    def search_product(self, product_id: int):
        product = self.products.get(product_id)
        product_name = product.get("name")
        product_stock = product.get("stock")
        product_price = product.get("price")

        print(f"Поиск товара: {product_name}")

        if product_stock == 0:
            print(f"Товар ID {product_id} закончился на складе.")
            multi = 0
        else:
            print(f"Товар ID {product_id}: {product}")
            multi = product_price * product_stock

        return product_id, multi

    def run(self):
        with self.execute as executor:
            futures = {
                executor.submit(self.search_product, product_id)
                for product_id in self.products
            }

            for future in concurrent.futures.as_completed(futures):
                product_id, multi = future.result()

                self.total_cost += multi
                print(f"Поиск завершён, статус: {future.done()}")

        print(f"Общая стоимость товаров на складе: {self.total_cost}")


dp = DataProduct(products)
dp.run()
