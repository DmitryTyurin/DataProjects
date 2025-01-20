# Нужно найти теги, подходящие по следующим условиям:
#     В начале тега стоит:
#     <p
#     Тут может быть последовательность символов минимально возможной длины
#     >
#     Внутри тега последовательность из любых символов минимально возможной длины
#     В конце тега стоит </p>

import re

pattern = r"<p[^>]*>(.*?)<\/p>"
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
        result = [i for i in result if len(i) > 0]
        result = [print(i, end="\n") for i in result]

        return result


r = RegularExpression(pattern, string)
r.get_result()
