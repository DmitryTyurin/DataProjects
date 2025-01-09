# Нужно найти последовательности, подходящие по следующим условиям:
# Состоит как минимум из 2-ух букв
# Используется латинский и кириллический алфавиты верхнего регистра

import re

regex = r"[A-ZА-ЯЁ]{2,}"


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
