# Найдите трёхзначные номера, перед которыми идёт №, Номер, или Number.
# Нужно найти последовательности, подходящие по следующим условиям:
#     Состоит из 3 арабских цифр
#     Слева от последовательности стоит №, Номер, или Number

import re

regex = r"(?:(?<=№\s)|(?<=Номер\s)|(?<=umber\s))(\d{3})"


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
