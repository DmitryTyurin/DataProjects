# Напишите регулярное выражение, которое разделит число из тестовых данных на числа, в конце которых стоит единица.
# Это число будет единицей, только если перед ним не будет других цифр.
# Все последовательности арабских цифр с минимально возможной длиной, заканчивающиеся на 1.

import re

regex = r"\d*?1"


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
