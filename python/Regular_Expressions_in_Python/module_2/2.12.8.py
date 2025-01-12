# Адрес представляет собой набор из префикса (1, или 3, или bc1) и основной части длиной от 27 до 34 символов.
# В основной части используются:
#     Весь латинский алфавит, кроме: O, I, l.
#     Все арабские цифры, кроме 0.

import re

regex = r"\b(1|3|bc1)[1-9A-HJ-NP-Za-km-z]{27,34}\b"


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
