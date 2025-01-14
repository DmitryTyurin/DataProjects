# Используются символы a-z, A-Z, 0-9, _
# Длина от 5 до 32 символов включительно
# Не может начинаться с цифры или _
# Не может заканчиваться на _
# На самом деле есть ещё одно условие: username не может содержать в себе __, но на данный момент сделать такое будет трудновато.

import re

regex = r"(?i)(?<!\S)[a-z0-9_]{5,32}(?!\S)"


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
