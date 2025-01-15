# Найти строку, в которой есть последовательности код или Код. Получить номер этой строки и номер начала вхождения последовательности.
# На вход программе подаются 4 строки.
# Выведите в консоль номер строки, в которой было найдено вхождение, и через пробел начальную позицию этого вхождения, если они были найдены.
# Иначе выведите строку: код не найден

import re
import sys

text = list(map(str.strip, sys.stdin.readlines()))
pattern = re.compile(r"код", re.IGNORECASE)


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, text: str, pattern):
        self.text = text
        self.pattern = pattern

    def get_result(self):
        for i, t in enumerate(self.text, start=1):
            match = self.pattern.search(t)
            if match:
                print(f"{i} {match.start()}")
                break
        else:
            print("код не найден")


r = RegularExpression(text, pattern)
r.get_result()
