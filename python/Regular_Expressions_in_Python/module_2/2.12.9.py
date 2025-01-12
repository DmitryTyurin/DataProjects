# Напишите регулярное выражение, которое найдёт следующие последовательности в тексте:
#     Привет, Олег
#     Привет, Григорий
#     Пока, Олег
#     Пока, Григорий

import re

regex = r"(?:Привет|Пока)\,\s(?:Олег|Григорий)"


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
