# Исправьте регулярное выражение, не используя атомарную группировку и притяжательные квантификаторы, чтобы у него не было Catastrophic Backtracking.

import re

regex = r'a+b'


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
