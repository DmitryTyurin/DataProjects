# Удалите все знаки препинания из текста и выведите количество совершённых замен.

import re
import sys

pattern = r"[.?!,:]"
string = input()

class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, pattern: str, string: str):
        self.string = string
        self.pattern = pattern

    def get_result(self):
        result = re.subn(self.pattern, "", self.string, flags=re.IGNORECASE)

        return result[1]


r = RegularExpression(pattern, string)
print(r.get_result())
