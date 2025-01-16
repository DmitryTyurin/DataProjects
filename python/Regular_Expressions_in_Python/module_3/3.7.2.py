# Нужно найти последовательности, подходящие по следующим условиям:
#     Начинается с https://imgur.com/
#     Потом идёт 7 симолов из следующего диапазона: a-z, A-Z, 0-9

import re
import sys

pattern = r"https:\/\/imgur\.com\/[\w\d]{7}"
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
