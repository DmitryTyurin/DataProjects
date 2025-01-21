# Нужно найти все числовые последовательности и заменить на их квадрат.

import re

pattern = r"(\d+)"
string = input()


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, pattern: str, string: str):
        self.string = string
        self.pattern = pattern

    def get_result(self):
        result = re.sub(self.pattern, lambda x: str(int(x.group())**2), self.string)

        return result


r = RegularExpression(pattern, string)
print(r.get_result())
