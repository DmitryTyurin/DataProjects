# Нужно заменить 2 повторяющиеся слова на одно:
#     Слова состоят из кириллических букв
#     Между ними стоит пробел
#     Если у слов разный регистр - слова разные

import re

pattern = r'\b(\w+)\s+\1\b'
string = input()


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, pattern: str, string: str):
        self.string = string
        self.pattern = pattern

    def get_result(self):
        result = re.sub(self.pattern, r'\1', self.string)

        return result


r = RegularExpression(pattern, string)
print(r.get_result())
