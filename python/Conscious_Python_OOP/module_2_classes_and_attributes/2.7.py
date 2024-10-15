# Создайте класс Coordinate и объявите в нём метод __init__.
# Метод __init__ будет создавать два атрибута x и y со значениями, которые вы укажите при создании экземпляра. Не забывайте указывать self.
# Создайте экземпляр coord и укажите координаты при создании в скобках, чтобы x и y стали равными 100 и 200 соответственно.
# Выведите на экран значения x и y в одну строку через пробел.


class Coordinate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


coord = Coordinate(100, 200)
print(coord.x, coord.y)


# Создайте класс Person.
# Объявите метод __init__ , который создаёт в экземпляре 4 атрибута: name, age, study, work. В скобках __init__ укажите 4 параметра с теми же именами, что и у атрибутов. И не забудьте про self.
# Если бы я создавал атрибут name, я бы сделал вот так: self.name = name.
# Создайте экземпляр класса id_1 и укажите в скобках Person() вот такие аргументы: 'Vasya', 22, 'college', 'developer'
# Выведите на экран __dict__ экземпляра id_1.


class Person:
    def __init__(self, name: str, age: int, study: str, work: str):
        self.name = name
        self.age = age
        self.study = study
        self.work = work


id_1 = Person("Vasya", 22, "college", "developer")

print(id_1.__dict__)


# Создайте класс BirthDay и объявите метод __init__. В параметрах __init__ укажите (self, present, color).
# Метод __init__ создаёт два атрибута present и color, и присваивает им значения параметров present, color соответственно. Объявите в методе создание этих атрибутов.
# Создайте три экземпляра Masha, Nikita, Lena и создайте у них атрибуты present, color соответственно тем подаркам, которые они подарят. Например Masha подарит, present = "pen", color = "red".
# Выведите на экран значения атрибутов у каждого экземпляра, согласно примеру ниже.
