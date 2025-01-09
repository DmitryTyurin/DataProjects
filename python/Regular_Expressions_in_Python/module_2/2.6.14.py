# Напишите регулярное выражение, которое найдёт все кабинеты с трёхзначным номером: 100 - 999.

import re

regex = r"[1-9]\d{2}\sкабинет"


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
