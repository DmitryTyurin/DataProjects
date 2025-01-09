# Нужно найти последовательности, подходящие по следующим условиям:
# Состоит из 3 букв
# Используется латинский и кириллический алфавиты верхнего и нижнего регистров
# Окружена пробелами с двух сторон

import re

regex = r"(?i)\s\b[a-zа-яёе]{3}\b\s"


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, regular: str, text: str):
        self.regular = regular
        self.text = text

    def get_result(self) -> str:
        result = re.findall(self.regular, self.text)
        result = " ".join(result)

        return result


r = RegularExpression(regex, input())
print(r.get_result())
