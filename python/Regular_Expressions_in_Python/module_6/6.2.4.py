# Все слова привет в тексте.

import re

pattern = r"привет"
string = input()


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, pattern: str, string: str):
        self.string = string
        self.pattern = pattern

    def get_result(self):
        result = re.findall(self.pattern, self.string, flags=re.IGNORECASE)

        return result


r = RegularExpression(pattern, string)
print(r.get_result())
