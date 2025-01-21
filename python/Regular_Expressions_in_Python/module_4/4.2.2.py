# Нужно названия html-тегов. Большинство html-тегов выглядит так:
#     В начале тега стоит < или </
#     В середине название тега, оно состоит из латинских букв нижнего регистра и арабских цифр максимальной длины
#     После названия может идти последовательность из любых символов минимальной длины
#     В конце тега стоит >

import re

pattern = r"(?:(?<=<)|(?<=</))(\w+)"
string = input()


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, pattern: str, string: str):
        self.string = string
        self.pattern = pattern

    def get_result(self):
        result = re.findall(self.pattern, self.string)

        return result


r = RegularExpression(pattern, string)
print(r.get_result())
