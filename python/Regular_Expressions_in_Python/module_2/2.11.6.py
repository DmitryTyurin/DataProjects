# Напишите регулярное выражение, которое найдёт все символы /, слева и справа от
# которых ничего нет или стоят другие символы, не равные /.
# Нужно найти последовательности, подходящие по следующим условиям:
#     Слева от неё не стоит /
#     Справа от неё не стоит /
#     Последовательность состоит из одного слеша: /

import re

regex = r"(?<!\/)\/{1}(?!\/)"


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
