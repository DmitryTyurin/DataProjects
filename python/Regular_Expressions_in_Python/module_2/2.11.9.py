# Напишите регулярное выражение, которое найдёт все неотрицательные числа.
# Нужно найти последовательности, подходящие по следующим условиям:
#     Состоит из арабских цифр
#     Перед последовательностью не стоит минус
#     Не является подпоследовательностью

import re

regex = r"(?<![\-\d])(?:\d+)"


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
