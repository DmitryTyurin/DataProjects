# Нужно найти последовательности, подходящие по следующим условиям:
# Состоит из цифр и ,
# В конце последовательности стоит  ₽

import re
import sys

pattern = r"[\d\,]+\s₽"
string = input()


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, pattern: str, string: str):
        self.string = string
        self.pattern = pattern

    def get_result(self):
        result = re.finditer(self.pattern, self.string, flags=re.IGNORECASE)
        result = [print(i.group(), end="\n") for i in result]


r = RegularExpression(pattern, string)
r.get_result()
