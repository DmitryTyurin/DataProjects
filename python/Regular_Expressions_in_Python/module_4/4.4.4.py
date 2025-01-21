# Нужно найти следующие последовательности:
#     Адрес состоит из любых числовых последовательностей, разделённых .
#     В середине стоит :
#     Порт является любой числовой последовательностью
#     и в начало к ним добавить протокол http://

import re

pattern = r"((?P<digit>\d+.){3}\d+:\d+)"
string = input()


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, pattern: str, string: str):
        self.string = string
        self.pattern = pattern

    def get_result(self):
        result = re.sub(self.pattern, r"http://\1", self.string)

        return result


r = RegularExpression(pattern, string)
print(r.get_result())
