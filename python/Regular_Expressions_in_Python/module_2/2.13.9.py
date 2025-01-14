# Нужно найти последовательности, подходящие по следующим условиям:
#     Используются буквы кириллического алфавита верхнего и нижнего регистров
#     В последовательности может содержаться дефис
#     Последовательность стоит в начале строки, если её нет - первого слова нет

import re

regex = r"(?i)^[а-яё\-]+"


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
