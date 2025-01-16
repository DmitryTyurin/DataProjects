# Найдите все последовательности цифр, которые начинаются от 13 цифр включительно.

import re
import sys

pattern = r"\b\d{13,}\b"
string = input()


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, pattern: str, string: str):
        self.string = string
        self.pattern = pattern

    def get_result(self):
        result = re.fullmatch(self.pattern, self.string)

        if result:
            return True
        else:
            return False


r = RegularExpression(pattern, string)
print(r.get_result())
