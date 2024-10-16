# Создайте два класса Minecraft и Roblox. Класс Roblox - будет дочерним классом Minecraft.
# В классе Minecraft создайте метод hello_creeper, который будет выводить на экран фразу - "Hello, Creeper!".
# В классе Roblox создайте метод hello_all, который будет вызывать метод hello_сreeper. Метод hello_all также будет выводить на экран фразу "Hello, Pozzy!" с помощью print.
# Создайте экземпляр hello класса Roblox.
# Вызовите метод hello_all, через экземпляр hello. Функцию print не нужно использовать.
from django.db.models.expressions import result


class Minecraft:
    def hello_creeper(self):
        print("Hello, Creeper!")


class Roblox(Minecraft):
    def hello_all(self):
        super().hello_creeper()
        print("Hello, Pozzy!")


hello = Roblox()
hello.hello_all()


# Создайте два класса Alfa и Beta (дочерний)
# В классе Alfa создайте статический метод sum_number используя декоратор @staticmethod. Метод sum_number имеет два параметра (x, y). Помните, что в статических методах не используется self. Сам метод возвращает сумму параметров
# x, y, используя return
# В дочернем классе Beta создайте обычный метод result, который имеет 4 параметра (self, x, y, z). Метод:
# записывает в переменную summa, результат вызова метода sum_number, используя параметры x, y.
# То есть summa = результат вызова sum_number.
# выводит на экран результат деления переменной summa на параметр z, с помощью print.
#        4. Создайте экземпляр test класса Beta
#        5. Вызовите метод result через экземпляр test, используя аргументы 10, 20, 30. Функцию print() использовать не нужно.


class Alfa:

    @staticmethod
    def sum_number(x: int, y: int) -> float:
        return float(sum([x, y]))


class Beta(Alfa):
    def result(self, x: int, y: int, z: int):
        summa = super().sum_number(x, y)

        print(summa // z)


test = Beta()
test.result(10, 20, 30)
