# Цель: Написать код, который будет обрабатывать предоставленную HTML-структуру, представляющую собой карточку товара. Код должен находить тег <p> с классом card-description и извлекать из него текстовое описание товара.
#
# Код должен:
#
# Обработать HTML ниже.
# Найти <p> с классом card-description.
# Извлечь текстовое описание товара из найденного тега.
# Вставьте код в поле ответа.

from bs4 import BeautifulSoup

HTML = """
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <title>Пример карточки товара</title>
        </head>
        <body>
            <div class="card">
                <img src="image.jpg" alt="Пример изображения товара">
                <h2 class="card-title"> iPhone 15 </h2>
                <p class="card-description">Аппаратной основой Apple iPhone 15 Pro Max стал 3-нанометровый чипсет A17 Pro с 6-ядерным GPU и поддержкой трассировки лучей. </p>
                <p class="card-price">999 999 руб.</p>
                <a href="https://example.com/product-link" class="card-link">Подробнее</a>
            </div>
        </body>
        </html>
"""


class DataSoup:
    def __init__(self, html: str):
        self.html = html
        self.soup = BeautifulSoup(self.html, "lxml")

    def get_description(self):
        return self.soup.p.text


ds = DataSoup(HTML)
print(ds.get_description())
