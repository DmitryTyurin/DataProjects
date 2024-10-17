# Создайте класс Number и объявите метод __init__. Метод имеет параметры (self, number), и создаёт атрибут number со значением number.
# Объявите метод __add__ (self, other) который позволяет складывать экземпляры с экземплярами, а также экземпляры с целыми числами. Учтите, что при сложении, будет складываться атрибут "number + number" двух экземпляров, и "number + целое число".
# Создайте два экземпляра num1 и num2, с атрибутом number равным 100 и 200 соответственно.
# Выведите на экран результаты трёх сложений, каждый на отдельной строке:
# num1 + num2
# num1 + 300
# num2 + 300
# Результат сложения будет число, смотрите пример ответа ниже.


class Number:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        if isinstance(other, Number):
            return self.number + other.number
        else:
            return self.number + other


num1 = Number(100)
num2 = Number(200)

print(num1 + num2)
print(num1 + 300)
print(num2 + 300)


# Создайте класс Number и объявите в нём два метода: __init__ и __sub__.
# Метод __init__(self, number) создаёт атрибут number со значением number
# Метод __sub__ должен позволять делать вычитание, в формате "экземпляр - экземпляр"
# Создайте два экземпляра num1 и num2, со значением number 70 и 20 соответственно.
# Выведите на экран результат вычитания num1 - num2


class Number:
    def __init__(self, number):
        self.number = number

    def __sub__(self, other):
        return self.number - other.number


num1 = Number(70)
num2 = Number(20)

print(num1 - num2)


# Допишите код, чтобы получить нужный результат.


class Hello:
    def __init__(self, say):
        self.say = say

    def __mul__(self, other):
        return self.say * other


lang = Hello("Hello!")
print(lang * 3)

# Создайте класс Number и объявите два метода: __init__ и __pow__
# Метод __init__(self, number) создаёт атрибут number со значением number
# Метод __pow__(self, power) возвращает результат возведения number в степень power
# Создайте экземпляр num, с атрибутом number равным числу 10
# Выведите на экран результат возведения экземпляра num в степень 2


class Number:
    def __init__(self, number):
        self.number = number

    def __pow__(self, power):
        return self.number**power


num = Number(10)
print(num**2)


# Создайте класс Number и объявите два метода: __init__ и __truediv__
# Метод __init__(self, number) создаёт атрибут number со значением number
# Метод __truediv__(self, other) возвращает результат деления number на other. Создайте проверку:
# - Если other является 0, верните строку "на ноль делить нельзя".
# - Если не 0, то просто верните результат деления number на other.
# Создайте экземпляр num, с атрибутом number равным числу 10
# Выведите на экран результат деления экземпляра num на число 2 и на 0. Два результата запишите на отдельных строках.


class Number:
    def __init__(self, number):
        self.number = number

    def __truediv__(self, other: [int, float] = 0):
        if other != 0:
            return self.number / other

        return "на ноль делить нельзя"


num = Number(10)
print(num / 2)
print(num / 0)


# Часть кода уже написан. Создайте нужные методы, чтобы все операции прошли корректно.


class Number:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other

    def __sub__(self, other):
        return self.number - other

    def __truediv__(self, other):
        return self.number / other

    def __mul__(self, other):
        return self.number * other

    def __pow__(self, other):
        return self.number**other

    def __abs__(self):
        return abs(self.number)


num1 = Number(-10)
result1 = num1 + 90
result2 = num1 / 10
result3 = num1 * -1
result4 = num1**2
result5 = num1 - 20
result6 = abs(num1)
print(result1, result2, result3, result4, result5, result6)
