# Нужно найти последовательности, подходящие по следующим условиям:
#     Состоит из букв латинского и кириллического алфавитов обоих регистров
#     Длина - 5 букв
#     Не является подпоследовательностью

import re
import sys

pattern = r"\b[a-zа-яё]{5}\b"
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
