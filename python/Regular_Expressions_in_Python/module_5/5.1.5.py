# Найти первое слово, состоящее из a-z в определённом диапазоне. Слово не может являться подпоследовательностью.
# На вход программе подаётся 3 строки:
#     Текст
#     Начальная позиция для поиска
#     Конечная позиция для поиска

import re

pattern = re.compile(r"\b[a-z]+\b")
string, start_pos, end_pos = input(), int(input()), int(input())


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, pattern, string: str, start_pos: int, end_pos: int):
        self.string = start_pos
        self.string = end_pos
        self.string = string
        self.pattern = pattern

    def get_result(self):
        result = pattern.search(string, start_pos, end_pos)

        if result:
            return result.group()
        else:
            return ""


r = RegularExpression(pattern, string, start_pos, end_pos)
print(r.get_result())
