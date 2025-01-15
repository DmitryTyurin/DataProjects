# Нужно найти первое слово в начале строки:
#     Состоит как минимум из одной буквы
#     Используются буквы латинского  алфавита обоих регистров

import re
import sys

pattern = re.compile(r"[a-z]+", re.IGNORECASE)
string = input()


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, pattern: str, string: str):
        self.string = string
        self.pattern = pattern

    def get_result(self):
        result = re.match(self.pattern, self.string)

        if result:
            return f"Первое слово в предложении: {result.group()}"
        else:
            return ""


r = RegularExpression(pattern, string)
print(r.get_result())
