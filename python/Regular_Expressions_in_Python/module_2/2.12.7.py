# Нужно найти последовательности, подходящие по следующим условиям:
#     Это последовательность да, нет, наверное
#     Не является подпоследовательностью

import re

regex = r"(?i)\b(?:да|нет|наверное)\b"


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
