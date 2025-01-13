# Нужно найти числа x, подходящие по следующим условиям:
#     x ∈ [0, 1] т.е. 0 ≤ x ≤ 1
#     x может быть как и десятичной дробью, так и целым числом
#     Если x - десятичная дробь, то её максимальная точность должна быть до сотых
#     В тестах не будет 0.00/0.0 или 1.00/1.0. Эти числа будут записаны без плавающей точки

import re

regex = r"(\b[01](?!\.\d)\b)|(?<!\w)(?:0\.[\d]{1,2})(?!\w)"


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
