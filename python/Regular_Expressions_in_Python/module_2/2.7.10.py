# Напишите регулярное выражение, которое найдёт все последовательности из любых пяти символов, кроме перехода на следующую строку.
# Нужно найти последовательности, подходящие по следующим условиям:
# Состоит из 5 символов
# Используются все символы, кроме перехода на новую строку

import re

regex = r"[^\n]{5}"


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
