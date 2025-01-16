# Нужно найти последовательности, подходящие по следующим условиям:
#     Начинается как минимум с одного из следующих символов: a-z, A-Z, 0-9, -, _
#     Потом идёт @
#     После @ снова идёт как минимум один из следующих символов: a-z, A-Z, 0-9
#     Потом идёт .
#     После . снова идёт как минимум один из следующих символов: a-z, A-Z, 0-9
#     Адрес почты не может быть подпоследовательностью.

import re
import sys

pattern = r"\b[\S\d\-\_]+@[\S\d]+[com|ru]\b"
string = input()


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, pattern: str, string: str):
        self.string = string
        self.pattern = pattern

    def get_result(self):
        result = re.findall(self.pattern, self.string, flags=re.IGNORECASE)

        [print(i) for i in result]


r = RegularExpression(pattern, string)
r.get_result()
