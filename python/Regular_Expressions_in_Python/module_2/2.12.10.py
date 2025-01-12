# Напишите регулярное выражение, которое найдёт следующие последовательности в тексте

import re

regex = r'((мы|вы|они)|(я|ты)|(она)|(он)) готов(?(2)ы|(?(3)а?|(?(4)а|)))\b'


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
