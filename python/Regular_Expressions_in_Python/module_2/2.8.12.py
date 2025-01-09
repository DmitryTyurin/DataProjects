# Напишите регулярное выражение, которое извлекает протокол полученной ссылки: http или https. Если протокола нет - ничего искать не надо.

import re

regex = r"\bhttp[s]?\b"


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
