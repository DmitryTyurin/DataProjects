# Нужно найти последовательности, подходящие по следующим условиям:
#     Часы от 0 до 23
#     Потом идёт :
#     Минуты от 0 до 59
#     Если в последовательности количество часов или минут меньше 10, то перед ним стоит 0
#     Не является подпоследовательностью

import re
import sys

pattern = r"\b(([01][\d]|2[0-3]):[0-5][\d])\b"
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

        [print(i[0]) for i in result]


r = RegularExpression(pattern, string)
r.get_result()
