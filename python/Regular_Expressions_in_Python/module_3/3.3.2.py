# Нужно найти первый хештег в тексте:
# Начинается с символа #
# После # стоит последовательность из латинских букв нижнего регистра

import re

regex = input()
regular = r"\#[a-z]*"


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, regex: str, regular: str):
        self.regex = regex
        self.regular = regular

    def get_result(self):
        result = re.search(self.regular, self.regex)

        if result:
            return result[0]
        else:
            return ""


r = RegularExpression(regex, regular)
print(r.get_result())
