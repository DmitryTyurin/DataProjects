# Нужно найти следующие последовательности:
#     Начинается и заканчивается с ** или *
#     В середине последовательность любой длины из букв кириллического и латинского алфавитов обоих регистров, а также пробелов
#     И заменить **text** на <strong>text</strong>, а *text* на <em>text</em>

import re

pattern = r'(\*{2}([\w\s]+?)\*{2})|(\*([\w\s]+?)\*)'
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
            if match.group(1):
                return '<strong>' + match.group(1) + '</strong>'
            else:
                return '<em>' + match.group(3) + '</em>'

        result = re.sub(self.pattern, replacement, self.string)

        return result


r = RegularExpression(pattern, string)
print(r.get_result())
