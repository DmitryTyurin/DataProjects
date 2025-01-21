# Нужно заменить все am на pm, а pm на am.

import re

pattern = r"(am|pm)"
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
            lambda x: "pm" if x.group(0) == "am" else "am",
            self.string,
            flags=re.IGNORECASE,
        )

        return result


r = RegularExpression(pattern, string)
print(r.get_result())
