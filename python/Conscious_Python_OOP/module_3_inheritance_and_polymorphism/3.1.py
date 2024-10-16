# Создайте класс Homer.
# Создайте в классе Homer метод __init__(self, name), который создает атрибут name.
# Создайте пустой класс Daughter и сделайте его дочерним классом для Homer. Используйте pass для пустого класса.
# Создайте экземпляр daughter1 для класса Daughter и присвойте атрибуту name значение Lisa.
# Выведите на экран значение атрибута name через экземпляр daughter1.
from pyasn1_modules.rfc2437 import pkcs_1


class Homer:
    def __init__(self, name):
        self.name = name


class Daughter(Homer):
    pass


daughter1 = Daughter("Lisa")
print(daughter1.name)


# Создайте класс CountDistance и объявите внутри него два метода: __init__() и dist_count().
# Метод __init__(self, x, y) создаёт атрибуты "x", "y" с соответствующими значениями.
# Метод dist_count(start, finish) будет статическим (@staticmethod). Метод будет принимать экземпляры, т.е. start - это экземпляр с данными x,y координат старта, а finish - это экземпляр с данными x,y координат конечной точки. Внутри метода создайте переменную dist = ((finish.x - start.x) ** 2 + (finish.y - start.y) ** 2) ** 0.5 - формула подсчитывает расстояние между точками. В итоге, метод выводит на экран округлённый результат round(dist) с помощью print.
# Создайте пустой класс Point (используя pass). Класс Point наследуется от класса CountDistance.
# Создайте экземпляр p1 класса Point, и присвойте во время создания атрибутам "x" и "y" - значения 10 и 20 соответственно.
# Создайте экземпляр p2 класса Point, и присвойте во время создания атрибутам "x" и "y" - значения 20 и 30 соответственно.
# Вызовите метод dist_count через класс CountDistance, в аргументах укажите (p1, p2). Функцию print использовать здесь не нужно. Данная команда подсчитает расстояние между точками p1, p2.


class CountDistance:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @staticmethod
    def dist_count(start, finish):
        dist = ((finish.x - start.x) ** 2 + (finish.y - start.y) ** 2) ** 0.5

        print(round(dist))


class Point(CountDistance):
    pass


p_1 = Point(10, 20)
p_2 = Point(20, 30)

CountDistance.dist_count(p_1, p_2)


# Код уже написан, но с ошибками. Подумайте, что можно поменять чтобы семейный статус выводился верно.
# В комментарии указано в какой области кода ошибка, внесите исправления именно там.
# В итоге команда print(masha.status) и print(vasya.status), должны выводить слова Дочь и Отец на отдельных строках. Код с выводом на экран написан правильно, его исправлять не нужно.


class Kondraty_Palich:
    status = "Деда"


class Vasya(Kondraty_Palich):
    status = "Отец"


class Masha(Kondraty_Palich):
    status = "Дочь"


# подумайте что можно поменять вот здесь:
masha = Masha()
vasya = Vasya()

# эту часть кода не исправляйте:
print(masha.status, vasya.status, sep="\n")
