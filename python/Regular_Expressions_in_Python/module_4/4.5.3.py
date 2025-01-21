# Нужно найти все слова, которые начинаются на букву А или а и заменить их на удалено(n), где n - длина удалённого слова.

import re

pattern = r"\bа\w*\b"
string = input()


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, pattern: str, string: str):
        self.string = string
        self.pattern = pattern

    def get_result(self):
        result = re.sub(
            self.pattern,
            lambda x: f"удалено({len(x.group(0))})",
            self.string,
            flags=re.IGNORECASE,
        )

        return result


r = RegularExpression(pattern, string)
print(r.get_result())
