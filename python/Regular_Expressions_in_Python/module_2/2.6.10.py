# Напишите регулярное выражение, которое найдет все последовательности: сон, сок, сом.

import re

regex = r"со[нкм]"


class RegularExpression:
    def __init__(self, regular: str, text: str):
        self.regular = regular
        self.text = text

    def findall(self) -> list:
        return re.findall(self.regular, self.text)


r = RegularExpression(regex, input())
print(r.findall())
