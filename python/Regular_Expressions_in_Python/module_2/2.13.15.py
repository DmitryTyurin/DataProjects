# Нужно найти последовательности, подходящие по следующим условиям:
#     Cостоит из символов латинского алфавита обоих регистров, цифр, а также _
#     Перед последовательностью стоит v=

import re

regex = r"(?i)(?<=v=)[a-z\d\_]+"


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
