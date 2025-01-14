# Как вы уже поняли - snake_case это тоже стиль наименования переменных. В Python переменные принято называть, используя этот стиль. Вот что он из себя представляет:
#     Всегда используется нижний регистр
#     Слова разделяются нижним подчёркиванием
#     Используются буквы латинского алфавита
#     Цифры в переменных из тестовых данных находятся только в конце.

import re

regex = r"\b(?:[a-z]+_?)+\d*\b"


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, regular: str, text: str):
        self.regular = regular
        self.text = text

    def get_result(self) -> str:
        result = re.findall(self.regular, self.text)
        result = " ".join(result)

        return result


r = RegularExpression(regex, input())
print(r.get_result())
