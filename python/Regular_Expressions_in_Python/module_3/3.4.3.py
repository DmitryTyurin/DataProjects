# Нужно проверить, может ли текст содержать seed-фразу:
#     Seed-фраза - это последовательность из 12, 18 или 24 случайных слов
#     В данном случае нужно проверять, что текст начинается как минимум с 12 слов
#     Слова состоят из букв латинского алфавита нижнего регистра
#     Между словами могут стоять только пробелы

import re
import sys

pattern = r"^[a-z]+(\s[a-z]+){11,23}$"
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
            return f"возможно, это seed-фраза"
        else:
            return ""


r = RegularExpression(pattern, string)
print(r.get_result())
