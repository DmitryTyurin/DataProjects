# Нужно найти последовательности, подходящие по следующим условиям:
#     Начинается с Категория:
#     Потом идёт последовательность из кириллических символов обоих регистров и пробелов
#     Минимальная длина последовательности 1 символ
#     Заканчивается на \n

import re
import sys

pattern = r"Категория:\s.[а-яё\s]{1,}\\n"
string = input()


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, pattern: str, string: str):
        self.string = string
        self.pattern = pattern

    def get_result(self):
        result = re.split(self.pattern, self.string, flags=re.IGNORECASE)

        return result


r = RegularExpression(pattern, string)
print(r.get_result())
