# Нужно найти последовательности, подходящие по следующим условиям:
#     Ссылка находится в теге a
#     Слева и справа от ссылки стоят двойные или одинарные кавычки
#     Перед левой кавычкой стоит href=
#     Сама ссылка может состоять из любых символов
#     Длина ссылки как минимум 1 символ
#     Попробуйте сначала найти все теги a, и только потом извлекайте из них ссылку.

import re
import sys

pattern = r"<a.+?href=\"(.+?)\""
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

        [print(i[1]) for i in result]


r = RegularExpression(pattern, string)
r.get_result()
