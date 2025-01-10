# Напишите регулярное выражение, которое найдёт все последовательности x с чётной длиной.
# Нужно найти последовательности, подходящие по следующим условиям:
#     Состоит из символов x
#     Длина последовательности чётная
#     Последовательность не может быть подпоследовательностью

import re

regex = r"\b(xx)+\b"


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
