# Создайте класс Rectangle, который принимает длину и ширину и позволяет вычислить площадь.


class Rectangle:
    def __init__(self, _length: int, _width: int):
        self.length = _length
        self.width = _width

    def area(self) -> int:
        return self.length * self.width


length, width = int(input()), int(input())

s = Rectangle(length, width)

print(s.area())


# Создайте класс Circle, который принимает радиус и вычисляет длину окружности.


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 2 * 3.14 * self.radius


r = int(input())
s = Circle(r)

print(s.area())


# Создайте класс Person, который принимает имя и возраст и позволяет получить информацию о человеке.


class Person:
    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age

    def get_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}")


name = input()
age = int(input())

person = Person(name, age)
person.get_info()


# Создайте класс Car, который принимает модель и год выпуска и позволяет узнать информацию об автомобиле.


class Car:
    def __init__(self, _model: str, _year: int):
        self.model = _model
        self.year = _year

    def info(self) -> None:
        print(f"Модель: {self.model}, Год выпуска: {self.year}")


model, year = input(), int(input())

car = Car(model, year)
car.info()


# Создайте класс Point, который принимает координаты x и y, и вычисляет расстояние от начала координат.
# Формулу необходимо загуглить)


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def distance(self) -> None:
        print(f"Расстояние от начала координат: {((self.x**2) + (self.y**2)) ** 0.5}")


num_1 = int(input())
num_2 = int(input())

s = Point(num_1, num_2)
s.distance()
