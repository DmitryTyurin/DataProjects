# Нужно найти переменные, записаные в стиле lowerCamelCase, который включает в себя следующее:
#     Первое слово начинается всегда с буквы нижнего регистра
#     Последующие слова начинаются с букв в верхнем регистре
#     Больше верхний регистр нигде не используется
#     Используются буквы латинского алфавита
#     Цифры в переменных из тестовых данных находятся только в конце


import re

regex = r"\b[a-z]+([A-Z]?[a-z]+)*[0-9]*\b"


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
