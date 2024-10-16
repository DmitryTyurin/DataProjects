# Допишите код так, чтобы на экран выводились слова, указанные в Sample Output. Для этого создайте метод __getattribute__ .


class User:
    def __init__(self, name):
        self.name = name + "man"

    def __getattribute__(self, item):
        return super().__getattribute__(item)


user1 = User("Super")
user2 = User("Bat")
user3 = User("Spider")

print(user1.name, user2.name, user3.name, sep="\n")


# Создайте класс Person и объявите метод __getattr__.
# В методе __getattr__ создайте условие проверки. Если имя атрибута равно 'name', создайте атрибут name со значением Vasya и верните его значение с помощью return. Иначе верните текст "Такого атрибута нет", с помощью return.
# Создайте экземпляр person
# Выведите на экран значение атрибута name через экземпляр person.


class Person:
    def __getattr__(self, item):
        if item == "name":
            self.name = "Vasya"
            return self.name
        else:
            return "Такого атрибута нет"


person = Person()
print(person.name)


# Создайте класс OnlyVasya и объявите в нём метод __setattr__.
# Внутри метода создайте условие. Если имя атрибута будет "name", то атрибуту с таким именем всегда будет устанавливаться значение "Vasya". Если имя атрибута другое, то будет стандартно устанавливаться значение атрибута. Подсказка, команда super().__setattr__(name, value) устанавливает значение атрибуту, подумайте как это можно использовать.
# Создайте экземпляр obj.
# Создайте атрибут name для экземпляра obj и присвойте ему значение "Masha".
# Выведите на экран значение атрибута name экземпляра obj.


class OnlyVasya:
    def __setattr__(self, name, value):
        if name == "name":
            super().__setattr__(name, "Vasya")
        else:
            super().__setattr__(name, value)


obj = OnlyVasya()
obj.name = "Masha"
print(obj.name)


# Создайте класс Number и объявите в нём два метода (__init__, __delattr__).
# Метод __init__ :
# - содержит параметры (self, a, b)
# - создаёт атрибуты "a", "b" с соответствующими значениями a, b
# - создаёт атрибут "s" который равен сумме "a + b"
# - удаляет атрибут "s"
# Метод __delattr__ :
# - содержит параметры (self, name)
# - содержит условие, если атрибут "s" больше 10, то ничего не делаем (pass). Иначе производим стандартное удаление с помощью super().__delattr__(name)
# Код проверки не удаляйте, пожалуйста


class Number:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.s = a + b
        del self.s

    def __delattr__(self, name):
        if self.s > 10:
            pass
        else:
            super().__delattr__(name)


# код проверки:
number1 = Number(4, 5)
print("s" in number1.__dict__)

number2 = Number(6, 11)
print("s" in number2.__dict__)
