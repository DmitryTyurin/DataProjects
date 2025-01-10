# Напишите регулярное выражение, которое найдёт все повторяющиеся последовательности из трёх цифр, которые идут друг за другом.
# Для этого используйте скобочные группы.
# Нужно найти последовательности, подходящие по следующим условиям:
#     В левой части любая последовательность из 3 арабских цифр
#     В правой части точно такая же последовательность

import re

regex = r"(\d{3})\1"


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
