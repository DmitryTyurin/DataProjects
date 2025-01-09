# Напишите регулярное выражение, которое найдёт все теги img в тексте.
# Нужно найти последовательности, подходящие по следующим условиям:
#     Начинается с <img
#     Заканчивается на >
#     Между началом и концом могут находиться последовательности из любых символов

import re

regex = r"<img.*?>"


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
