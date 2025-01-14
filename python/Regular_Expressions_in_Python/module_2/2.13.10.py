# Нужно найти последовательности, подходящие по следующим условиям:
#     Состоит из букв латинского алфавита нижнего и верхнего регистров, -
#     Начинается на n или N
#     Не может быть подпоследовательностью

import re

regex = r"(?i)\b(?<![a-z-])[nN].[a-z-]+\b"


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
