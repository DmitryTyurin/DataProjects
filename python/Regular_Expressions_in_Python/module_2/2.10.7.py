# Напишите регулярное выражение, которое найдёт все повторяющиеся последовательности из двух цифр, которые идут друг за другом.
# Используйте нумерованные группы. Нужно найти последовательности из 2 одинаковых арабских цифр

import re

regex = r"(\d{2})\1"


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
