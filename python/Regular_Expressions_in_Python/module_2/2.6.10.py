# Напишите регулярное выражение, которое найдет все последовательности: сон, сок, сом.

import re

regex = r"со[нкм]"


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """
    def __init__(self, regular: str, text: str):
        self.regular = regular
        self.text = text

    def findall(self) -> str:
        result = re.findall(self.regular, self.text)
        result = ' '.join(result)

        return result


r = RegularExpression(regex, input())
print(r.findall())
