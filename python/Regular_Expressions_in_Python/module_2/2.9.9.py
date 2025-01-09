# Напишите регулярное выражение, которое найдёт все последовательности символов, окруженные двойными кавычками.
# Нужно найти последовательности, подходящие по следующим условиям:
#     В начале и в конце последовательности стоят двойные кавычки: "
#     Между кавычками могут находиться последовательности из любых символов
#     Между кавычками стоит как минимум один символ
#     Длина последовательности должна быть минимально возможной

import re

regex = r"[\"].*?[\"]"


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
