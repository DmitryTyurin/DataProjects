# Цель: Необходимо написать код, который будет обрабатывать HTML-структуру с карточками товаров (в данном случае — книг). Код должен вычислять общую сумму, которую можно получить при продаже всех книг на складе.
# HTML-строка, содержащая структуру с карточками товаров. Каждая карточка товара имеет следующий вид:
#
# <div class="book-card">
#     <p class="count price">Цена: $[цена]</p>
#     <p class="count stock">Количество на складе: [количество]</p>
#     <!-- ... остальные элементы карточки ... -->
# </div>
#  где [цена] — это стоимость одной единицы товара, а [количество] — это количество товара на складе.
#
# Задача:
#
# Извлечь из каждой карточки информацию о цене и количестве на складе.
# Умножить цену на количество для каждого товара.
# Подсчитать общую сумму для всех товаров.
# Выходные данные:
#
# Общая сумма, которую можно выручить при продаже всех книг.
#
# Требования к реализации:
#
# Использовать библиотеку BeautifulSoup для обработки HTML.
# Учесть возможное наличие двойных тегов.
# Код должен быть написан так, чтобы легко масштабироваться для обработки любого количества карточек товаров.
# Функция calculate_total_price() принимает на вход документ html и должна вернуть искомое значение.
# Нужно вывести сообщение с итогом работы программы
# print(f"Общая стоимость в случае продажи всех товаров: ${calculate_total_price(html)}")


from bs4 import BeautifulSoup
import requests

URL = "https://parsinger.ru/4.3/5/index.html"


class DataSoup:
    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup(self.get_html(), "lxml")
        self.total_sum = []

    def get_html(self):
        response = requests.get(self.url)
        response.encoding = "utf-8"

        response.raise_for_status()

        if response.status_code == 200:
            return response.text
        else:
            return None

    @staticmethod
    def extract_digits(text):
        import re

        pattern = r"\d{1,}\.\d{1,}|\d{1,}"
        digits = "".join(re.findall(pattern, text))

        return digits

    def get_books(self):
        data = self.soup.find_all("div", attrs={"class": "book-card"})

        return data

    def get_count(self, data, class_name):
        data = data.find("p", attrs={"class": class_name})

        text_data = data.get_text(strip=True)
        text_data = self.extract_digits(text_data)

        return float(text_data)

    def calculate_total_price(self):
        book_cards = self.get_books()

        for card in book_cards:
            count_price = self.get_count(card, "count price")
            count_stock = self.get_count(card, "count stock")

            self.total_sum.append(round(count_price * count_stock, 2))

        print(
            f"Общая стоимость в случае продажи всех товаров: ${sum(self.total_sum):.2f}"
        )


def main():
    ds = DataSoup(URL)
    ds.calculate_total_price()


main()
