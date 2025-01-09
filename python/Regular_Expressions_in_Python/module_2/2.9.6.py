# Составьте регулярное выражение, которое найдёт все чётные числа в тестовой строке.
# Все чётные числа с минимально возможной длиной.
# В десятичной системе счисления все числа, которые заканчиваются на чётную цифру - чётные.

import re

regex = r"\d*?[02468]"


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
