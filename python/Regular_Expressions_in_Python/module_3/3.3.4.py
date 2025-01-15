# Нужно найти первый попавшийся ключ. Нужные ключи в чате всегда отправляют в виде:
#     Activation key: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
#     X - любая цифра или латинская буква в верхнем регистре
#     Перед нужным ключом должна стоять строка Activation key:

import re
import sys

text = [input().strip() for _ in range(5)]
pattern = r"(?<=Activation key: )(?:[A-Z\d]{5}-){4}[A-Z\d]{5}"


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, text: list, pattern):
        self.text = text
        self.pattern = pattern

    def get_result(self):
        for t in self.text:
            result = re.search(self.pattern, t)

            if result:
                return result.group(0)


r = RegularExpression(text, pattern)
print(r.get_result())
