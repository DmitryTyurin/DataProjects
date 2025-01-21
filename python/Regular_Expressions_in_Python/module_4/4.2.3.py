# Нужно найти логин, пароль, и токен:
#     Логин состоит из 0-9
#     Пароль состоит из a-z, A-Z, 0-9
#     Токен состоит из a-z, 0-9
#     Длина минимум 1 символ

import re

pattern = r"(?P<login>\d+):(?P<password>[a-zA-Z\d]+):(?P<token>[a-z\d]+)"
string = input()


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, pattern: str, string: str):
        self.string = string
        self.pattern = pattern

    def get_result(self):
        result = re.findall(self.pattern, self.string)

        return result


r = RegularExpression(pattern, string)
print(r.get_result())
