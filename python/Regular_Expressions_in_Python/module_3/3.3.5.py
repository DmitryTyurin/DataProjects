# Нужно найти ключ t и его значение:
#     Значением является последовательностью из арабских цифр, символов . и +
#     Перед значением стоит t=

import re
import sys

text = input()
pattern = re.compile(r"(t\=[\d\.\+]+)", re.IGNORECASE)


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, text: str, pattern):
        self.text = text
        self.pattern = pattern

    def get_result(self):
        result = re.search(self.pattern, self.text)

        return result.group(0)


r = RegularExpression(text, pattern)
print(r.get_result())
