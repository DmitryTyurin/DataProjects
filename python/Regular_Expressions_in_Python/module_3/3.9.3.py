# Нужно удалить все теги в html-разметке:
#     Начинается с <
#     Потом идёт последовательность любых символов любой длины
#     Заканчивается с >

import re
import sys

pattern = r"<.*?>"
string = input()


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, pattern: str, string: str):
        self.string = string
        self.pattern = pattern

    def get_result(self):
        result = re.sub(self.pattern, "",self.string, flags=re.IGNORECASE)

        return result


r = RegularExpression(pattern, string)
print(r.get_result())
