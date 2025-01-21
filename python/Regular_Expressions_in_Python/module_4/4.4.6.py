# Нужно найти следующие последовательности:
#     Начинается с его/её/их или Его/Её/Их
#     Потом идёт последовательность кириллических букв максимальной длины
#     и убрать из них ненужную часть.

import re

pattern = r"([Ее]го|[Ее]ё|[Ии]х)\w+"
string = input()


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, pattern: str, string: str):
        self.string = string
        self.pattern = pattern

    def get_result(self):
        result = re.sub(self.pattern, r"\1", self.string)

        return result


r = RegularExpression(pattern, string)
print(r.get_result())
