# Замените все цифры на X. Выведите полученную строку и количество совершённых замен.

import re
import sys

pattern = r"\d"
string = input()

class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, pattern: str, string: str):
        self.string = string
        self.pattern = pattern

    def get_result(self):
        result = re.subn(self.pattern, "X", self.string, flags=re.IGNORECASE)

        return result


r = RegularExpression(pattern, string)
print(r.get_result())
