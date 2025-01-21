# Нужно найти следующие последовательности:
#     Дата типа mm/dd/yyyy
#     mm, dd, yyyy - любые числовые последовательности длиной 2, 2, 4 соответственно
#     Между ними стоят разделители . или /
#     и переставить mm с dd местами, чтобы получилась дата вида dd/mm/yyyy

import re

pattern = r"(\d{2})([/.])(\d{2})[/.](\d{4})"
string = input()


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, pattern: str, string: str):
        self.string = string
        self.pattern = pattern

    def get_result(self):
        def replacement(match):
            month, split, day, year = match.groups()

            return f"{day}{split}{month}{split}{year}"

        result = re.sub(self.pattern, replacement, self.string)

        return result


r = RegularExpression(pattern, string)
print(r.get_result())
