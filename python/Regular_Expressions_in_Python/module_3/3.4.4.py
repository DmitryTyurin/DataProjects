# Вывести всё содержимое, до символа @

import re
import sys

pattern = re.compile(r".*(?=@)", re.IGNORECASE)
string = input()


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, pattern: str, string: str):
        self.string = string
        self.pattern = pattern

    def get_result(self):
        result = re.match(self.pattern, self.string)

        if result:
            return result.group()
        else:
            return ""


r = RegularExpression(pattern, string)
print(r.get_result())
