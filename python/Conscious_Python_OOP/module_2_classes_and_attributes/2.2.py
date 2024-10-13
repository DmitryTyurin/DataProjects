# Создайте класс Person
# Создайте атрибут name внутри класса, и присвойте ему значение "Vasya"
# Создайте экземпляр класса и назовите его id_1. Не забывайте про скобки у класса.
# Выведите на экран значение атрибута name, который принадлежит экземпляру id_1, используя print()


class Person:
    name = "Vasya"


id_1 = Person()
print(id_1.name)


# Создайте класс Person.
# Создайте в классе Person, атрибут name со значением "Vasya".
# Создайте экземпляр id_1 класса Person.
# Создайте в экземпляре id_1, атрибут name со значением "Lena".
# Измените в классе Person атрибут name на значение "Masha".
# Выведите на экран значение атрибута name класса Person, и экземпляра id_1 с помощью print. Каждый результат на отдельной строке, сначала у Person, затем у id_1 (см. пример ниже).


class Person:
    name = "Vasya"


id_1 = Person()
id_1.name = "Lena"
Person.name = "Masha"
print(Person.name)
print(id_1.name)


# Создайте пустой класс Сoordinate (используйте pass).
# Создайте экземпляр coord класса Сoordinate.
# Создайте атрибут "x" в экземпляре coord, со значением 100.
# Измените атрибут "x"  в экземпляре coord на число 5.
# Выведите на экран значение атрибута "x" экземпляра coord, с помощью print.


class Coordinate:
    pass


coord = Coordinate()
coord.x = 100
coord.x = 5
print(coord.x)


# Создайте пустой класс Holiday (используйте pass внутри класса).
# Создайте экземпляр friends.
# Создайте 5 атрибутов для экземпляра friends, с именами name1, name2...name5 со значениями 'Sveta', 'Katya', 'Lena', 'Natasha', 'Leonardo DiCaprio' соответственно.
# Так как 'Leonardo DiCaprio' не смог прийти, Машенька приглашает вас на свой ДР. Измените атрибут name5 на своё имя, или можете использовать любое другое имя.
# Часть кода уже написана, вам нужно лишь сделать то, что написано в задании.


class Holiday:
    pass


friends = Holiday()
friends.name1 = "Sveta"
friends.name2 = "Katya"
friends.name3 = "Lena"
friends.name4 = "Natasha"
friends.name5 = "Leonardo DiCaprio"
friends.name5 = "Dmitry"
print(friends.name5)
