# Многие функции возвращают None в результате своей работы, если ничего не было найдено.
# Попробуйте вывести нулевую группу в Match-объекте, если совпадение было найдено. Если его нет - ничего не выводите.

import re

match = re.match(input(), input())


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, match):
        self.match = match

    def get_result(self):
        if self.match:
            return self.match.group(0)
        else:
            return ""


r = RegularExpression(match)
print(r.get_result())
