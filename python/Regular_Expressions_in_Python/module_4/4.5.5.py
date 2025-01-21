# Найти все числа в тексте, и проверить, кратно число 3 или нет:
# Если кратно, то заменить его на это же число, разделённое на 3
# Если нет - оставить его как есть

import re

pattern = r"(\d+)"
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
            lambda x: str(int(x[0])) if int(x[0]) % 3 else str(int(x[0]) // 3),
            self.string,
        )

        return result


r = RegularExpression(pattern, string)
print(r.get_result())
