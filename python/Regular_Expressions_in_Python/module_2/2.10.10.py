# Напишите регулярное выражение, которое найдёт все последовательности if и <if>, но не <if и if>, стоящие между началом и концом строки.

import re

regex = r"^(?:if|<if>)$"


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
