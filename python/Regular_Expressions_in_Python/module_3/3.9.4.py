# Нужно найти все ФИО в тексте и заменить их на строку ФИО.
#     ФИО могут быть двух видов:
#     Фамилия Имя Отчество
#     Фамилия И. О.
#     Также ФИО могут склоняться.  Генерируйте регулярное выражение "на ходу".

import re
import sys

fio = input().split()
f1, i1, o1 = fio[0], fio[1][0] + ".", fio[2][0] + "."
f2, i2, o2 = fio[0], fio[1][:-1], fio[2]

pattern = rf"({f1}[а-я]*?[ ]{i1}[ ]{o1})|({f2}[а-я]*?[ ]{i2}[а-я]*?[ ]{o2}[а-я]*?)\b"
string = input()


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, pattern: str, string: str):
        self.string = string
        self.pattern = pattern

    def get_result(self):
        result = re.sub(self.pattern, "ФИО", self.string, flags=re.IGNORECASE)

        return result


r = RegularExpression(pattern, string)
print(r.get_result())
