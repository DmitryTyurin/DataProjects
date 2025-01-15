# В переменной match записан объект Match. Выведите на экран:
#     Его нулевую группу
#     Начало вхождения нулевой группы
#     Конец вхождения нулевой группы
#     Атрибут pos
#     Атрибут endpos
#     Атрибут re
#     Атрибут string
#     На входные данные и функцию re.match() не обращайте внимания.

import re

match = re.match(input(), input())


class RegularExpression:
    """
    Класс для работы с регулярными выражениями
    """

    def __init__(self, match):
        self.match = match

    def get_result(self):
        print(self.match.group(0))
        print(self.match.start())
        print(self.match.end())
        print(self.match.pos)
        print(self.match.endpos)
        print(self.match.re)
        print(self.match.string)


r = RegularExpression(match)
r.get_result()
