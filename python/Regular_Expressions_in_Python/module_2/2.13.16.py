# Нужно найти последовательности, подходящие по следующим условиям:
#     Начинается с [ и заканчиваются на ]
#     Внутри может быть пусто, а могут находиться числа
#     Числом считаем произвольную последовательность из цифр
#     Между числами должны стоять запятые
#     Запятые могут быть как и с пробелом, так и без
#     После последнего числа может стоять запятая, т.к. такие массивы: [123, 123, ] и [23, ] валидные в Python

import re

regex = r"(?i)\[(\d+(,\s*\d*)*,?\s*|\s*)]"


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
