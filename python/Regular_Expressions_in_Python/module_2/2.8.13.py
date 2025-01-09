# Напишите регулярное выражение, которое найдёт все "числа", написанные с помощью римских цифр.
# Нужно найти последовательности, состоящие из римских цифр: IVXLCDM.

import re

regex = r"\b[IVXLCDM]+\b"


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
