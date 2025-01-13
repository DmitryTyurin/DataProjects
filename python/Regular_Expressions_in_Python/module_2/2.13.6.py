# Нужно найти последовательности, подходящие по следующим условиям:
#     Используются буквы кириллического алфавита нижнего и верхнего регистров
#     Последовательность должна содержать как минимум одну букву а
#     Заглавную А искать не нужно
#     Последовательность не может быть подпоследовательностью

import re

regex = r"(?i)\b[a-я]*[а][a-я]*\b"


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
