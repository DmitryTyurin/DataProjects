# Нужно разделить строку по символвам ? и &, оставив эти символы в полученном списке.

import re

pattern = r"([?&])"
string = input()


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, pattern: str, string: str):
        self.string = string
        self.pattern = pattern

    def get_result(self):
        result = re.split(self.pattern, self.string)

        return result


r = RegularExpression(pattern, string)
print(r.get_result())
