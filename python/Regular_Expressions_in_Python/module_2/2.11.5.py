# Напишите регулярное выражение, которое получит последовательность из любых символов от [^START] до {(END.)}.
# Нужно найти последовательности, подходящие по следующим условиям:
#     Слева от неё стоит [^START]
#     Справа от неё стоит {(END.)}
#     Состоит из любых символов, кроме символа перехода на новую строку

import re

regex = r"(?<=\[\^\S{5}\])\S.*(?=\{\(\S{3}\.\)\})"


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, regular: str, text: str):
        self.regular = regular
        self.text = text

    def get_result(self) -> str:
        result = re.findall(self.regular, self.text)
        result = " ".join(result)

        return result


r = RegularExpression(regex, input())
print(r.get_result())
