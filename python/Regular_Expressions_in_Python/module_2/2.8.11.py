# Напишите регулярное выражение, которое найдёт все адреса ETH кошельков.
# Адрес ETH кошельков состоит из двух частей:
#     0x
#     Длина 40 символов
# Используются все символы шестнадцатеричной системы счисления в нижнем и верхнем регистрах

import re

regex = r"0x[0-9a-fA-F]{40}"


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
