# Смайлик состоит из трёх частей: глаз, носа (который может отсутствовать) и рта. В них используются следующие символы:
# Глаза: :8;¦=
# Нос: ^-
# Рот: |\0()/PODIC

import re

regex = r"[:8;¦=][\^-]?[\|\0()/PODIC]"


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
