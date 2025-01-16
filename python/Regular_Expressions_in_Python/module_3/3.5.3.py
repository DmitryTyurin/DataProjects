# Проверить пароль на валидность. Валидным будем считать пароль, который:
#     Состоит из a-z, A-Z, 0-9, @#$%^&*()_-+!?
#     Его длина минимум 8 символов

import re
import sys

pattern = re.compile(r"[\w@#$%^&*()_\-+!?]{8,}", re.IGNORECASE)
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
