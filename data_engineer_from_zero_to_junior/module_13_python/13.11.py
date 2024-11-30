# Создайте класс Rectangle, который принимает длину и ширину и позволяет вычислить площадь.


class Rectangle:
    def __init__(self, _length:int, _width: int):
        self.length = _length
        self.width = _width

    def area(self) -> int:
        return self.length * self.width


length, width = int(input()), int(input())

s = Rectangle(length, width)
print(s.area())
