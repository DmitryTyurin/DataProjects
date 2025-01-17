import re
import sys

string = rf"{input()}"


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, string: str):
        self.string = string

    def get_result(self):
        result = re.escape(self.string)

        return result


r = RegularExpression(string)
print(r.get_result())
