# [12346789] Сверху дано регулярное выражение. Запишите его сокращённую версию в переменную regex.

import re

regex = r"[1-4]|[6-9]"


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
