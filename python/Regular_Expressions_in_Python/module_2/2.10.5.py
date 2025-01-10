# Напишите регулярное выражение, которое найдёт все повторяющиеся буквы в тексте.
# Нужно найти последовательности, подходящие по следующим условиям:
#     Последовательность из 2 одинаковых букв
#     Используются буквы латинского и кириллического алфавитов нижнего и верхнего регистров

import re

regex = r"(?i)([a-zа-яё])\1"


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
