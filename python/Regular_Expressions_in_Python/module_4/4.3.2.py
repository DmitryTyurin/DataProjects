# Нужно разделить строку по следующей последовательности:
#     В левой части нечисловая последовательность символов любой длины
#     В  середине стоит один из символов +:=*/-
#     В правой части нечисловая последовательность символов любой длины

import re

pattern = r"[^+:=*/\-+\d]+"
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
