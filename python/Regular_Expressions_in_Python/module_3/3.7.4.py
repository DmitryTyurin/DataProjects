# Найдите все даты в тексте. Датой в этом задании будем считать любую последовательность:
#     nn/nn/nnnn
#     nnnn/nn/nn
#     nn.nn.nnnn
#     nnnn.nn.nn

import re
import sys

pattern = r"(\d{4}[\.]\d{2}[\.]\d{2}|(\d{2}[\.]){2}\d{4})|(\d{4}[\/]\d{2}[\/]\d{2}|(\d{2}[\/]){2}\d{4})"
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

        [
            print(value)
            for tuple in result
            for value in tuple
            if str(value).count(".") == 2 or str(value).count("/") == 2
        ]


r = RegularExpression(pattern, string)
r.get_result()
