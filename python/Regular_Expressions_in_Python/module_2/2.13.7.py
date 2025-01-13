# Нужно найти последовательности, подходящие по следующим условиям:
#     Состоит из букв кириллического алфавита нижнего и верхнего регистра
#     После последовательности стоит один из знаков препинания: .,:?!;


import re

regex = r"(?i)\b[a-яё]+(?=[.,:?!;])\b"


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
