# Найдите все последовательности, которые могут быть номерами телефонов:
#     Номер может начинаться с +
#     Потом идут цифры
#     В каждом номере минимум 11 цифр
#     Между цифрами могут быть разделители: ( )-
#     Длина разделителя от 0 до 2 символов включительно

import re
import sys

pattern = re.compile(r"\+?(\d[( )-]{0,2}){11,}", re.IGNORECASE)
string = input()


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, pattern: str, string: str):
        self.string = string
        self.pattern = pattern

    def get_result(self):
        result = re.fullmatch(self.pattern, self.string)

        if result:
            return True
        else:
            return False


r = RegularExpression(pattern, string)
print(r.get_result())
