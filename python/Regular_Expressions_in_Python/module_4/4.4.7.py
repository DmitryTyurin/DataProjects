# Нужно найти первую цену в тексте:
#     Любая числовая последовательность
#     В конце стоит ₽$
#     и подставить её в строку Цена данного товара x.

import re

pattern = r"(\d+[₽$])"
string = input()


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, pattern: str, string: str):
        self.string = string
        self.pattern = pattern

    def get_result(self):
        result = re.search(self.pattern, self.string)

        if result is None:
            return ""
        else:
            return result.expand(r"Цена данного товара \1")


r = RegularExpression(pattern, string)
print(r.get_result())
