# Напишите регулярное выражение, которое найдёт все слова «Ты» или «ты». Другие формы слова «ты», такие как «твой» и т. д. учитывать не следует.
# Нужно найти последовательности, подходящие по следующим условиям:
#     Последовательность ты или Ты
#     Не является подпоследовательностью

import re

regex = r"(?i)\bты\b"


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
