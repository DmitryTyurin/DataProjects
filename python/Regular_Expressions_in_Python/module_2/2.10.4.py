# Напишите регулярное выражение, которое найдёт все слова и словосочетания, состоящие из двух одинаковых частей.
# Между одинаковыми половинами слова может стоять дефис.
# Нужно найти последовательности, подходящие по следующим условиям:
#     В левой части любая последовательность букв кириллического алфавита нижнего регистра
#     В правой части точно такая же последовательность
#     Между ними может стоять тире
#     Последовательность не может быть подпоследовательностью

import re

regex = r"(?i)\b([а-яё]+)-?\1\b"


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
