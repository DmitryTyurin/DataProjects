# Напишите регулярное выражение, которое найдёт все квадратные скобки и их содержимое.
# Нужно найти последовательности, подходящие по следующим условиям:
# В начале и в конце последовательности стоят квадратные скобки
# Между квадратными скобками могут находиться последовательности из любых символов
# Длина последовательности должна быть минимально возможной

import re

regex = r"\[.*?\]"


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
