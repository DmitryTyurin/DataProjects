# Цель: Написать код, который будет обрабатывать HTML-структуру, содержащую карточки товаров. Код должен находить все теги с классом card-articul, извлекать из них числовые значения артикулов и суммировать их.
#
# Код должен:
#
# Обработать HTML по ссылке или под спойлером.
# Обработать все теги <p> с классом card-articul в предоставленном HTML.
# Извлечь числовое значение артикула из тега <p>, следующее после текста "Артикул: ".
# Суммировать все извлеченные числовые значения.
# Пример:
#
# <p class="card-articul">Артикул: 104774</p>
# <p class="card-articul">Артикул: 105550</p>
# <p class="card-articul">Артикул: 106200</p>


from bs4 import BeautifulSoup

HTML = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
    </head>
    <body>
        <div class="cards">
            <!-- Карточка товара 1 -->
            <div class="card">
                <img src="parsing.png" alt="WEB Парсинг на Python">
                <h2 class="card-title">WEB Парсинг на Python</h2>
                <p class="card-articul">Артикул: 104774</p>
                <p class="card-stock">Наличие: 5 шт.</p>
                <p class="card-price">3500 руб.</p>
                <a href="https://stepik.org/a/104774" class="card-button">Купить</a>
            </div>
            <!-- Карточка товара 2 -->
            <div class="card">
                <img src="async.png" alt="Асинхронный Python">
                <h2 class="card-title">Асинхронный Python</h2>
                <p class="card-articul">Артикул: 170777</p>
                <p class="card-stock">Наличие: 10 шт.</p>
                <p class="card-price">3500 руб.</p>
                <a href="https://stepik.org/a/170777" class="card-button">Купить</a>
            </div>
            <!-- Карточка товара 3 -->
            <div class="card">
                <img src="selenium.PNG" alt="Selenium Python">
                <h2 class="card-title">Selenium Python</h2>
                <p class="card-articul">Артикул: 119495</p>
                <p class="card-stock">Наличие: 5 шт.</p>
                <p class="card-price">1250 руб.</p>
                <a href="https://stepik.org/a/119495" class="card-button">Купить</a>
            </div>
        </div>
    </body>
    </html>
"""


class DataSoup:
    def __init__(self, html: str):
        self.html = html
        self.soup = BeautifulSoup(self.html, "lxml")
        self.articul_list = []

    def get_articul(self):
        card_articul_all = self.soup.find_all("p", class_="card-articul")

        for card_articul in card_articul_all:
            text = card_articul.text
            text = int(text.replace("Артикул: ", ""))

            self.articul_list.append(text)

    def get_sum(self):
        sum_articuls = sum(self.articul_list)

        print(f"Сумма артикулов: {sum_articuls}")


def main():
    ds = DataSoup(HTML)
    ds.get_articul()
    ds.get_sum()


main()
