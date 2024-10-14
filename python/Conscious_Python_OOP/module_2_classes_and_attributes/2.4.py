# Создайте класс Kitty.
# Создайте метод say_hello (не забудьте про self).
# Внутри метода создайте print('Hello, Kitty'). Метод выводит на экран строку 'Hello, Kitty'.
# Создайте экземпляр cat.
# Вызовите метод say_hello через экземпляр cat (не забудьте скобки). Функцию print здесь использовать не нужно.


class Kitty:
    def say_hello(self):
        print("Hello, Kitty")


cat = Kitty()

cat.say_hello()


# Часть кода уже написана.
# Создайте метод и назовите его как пожелаете. Помните, что имя метода означает - глагол, действие, поэтому подберите соответствующее название.
# Метод выводит на экран надпись: "Привет, атрибут".
# Но слово "атрибут" замените, на значение атрибута name у экземпляров.
# У каждого экземпляра свой атрибут name, поэтому и сообщения будут выводиться разными.
# Подсказка, можно использовать f-строку и не забудьте self.
# Вызовите метод у каждого экземпляра. Не забывайте скобки, при вызове метода.
# Примеры ответов есть ниже.


class Simpsons:
    name = "Simpsons"

    def get_name_attribute(self):
        print(f"Привет, {self.name}")


bart = Simpsons()
lisa = Simpsons()
homer = Simpsons()

bart.name = "Bart"
lisa.name = "Lisa"
homer.name = "Homer"

bart.get_name_attribute()
lisa.get_name_attribute()
homer.get_name_attribute()


# Создайте метод print_number_of_Persons(). Метод выводит на экран значение атрибута Person_counter. У каждого экземпляра свой атрибут Person_counter, поэтому используйте self.
# В самом конце, выведите на экран количество сообщений у экземпляра id_1 и id_2. Каждый ответ на отдельной строке (см. пример ответа ниже).
class Person:
    message_counter = 0

    def print_number_of_messages(self):
        print(self.message_counter)


id_1 = Person()
id_2 = Person()

id_1.message_counter = 5
id_2.message_counter = 10

id_1.print_number_of_messages()
id_2.print_number_of_messages()


# Создайте класс NewJournal.
# Объявите два метода: set_attr() и check_money().
# Метод set_attr():
# - Имеет 4 параметра: papa, mama, deda, baba. Это значит set_attr(self, papa, mama...и т.д.).
# - Создаёт атрибуты papa, mama, deda, baba, а значения этих атрибутов будут равны параметрам papa, mama, deda, baba, соответственно. Например self.papa = papa.
# - Создаёт атрибут count_money равный сумме этих четырёх атрибутов: papa, mama, deda, baba.
# Метод check_money():
# - Проверяет, если атрибут count_money меньше 80, то выводит на экран: Денег не хватает
# - Иначе выводит на экран: Ура, денег хватает!
# Создайте экземпляр masha.
# Вызовите метод set_attr() через экземпляр masha. В аргументах укажите 10, 20, 30, 40 - это наши значения для атрибутов: papa, mama, deda, baba.
# Вызовите метод check_money()
# Не забывайте про self и скобки при вызове методов.


class NewJournal:
    def set_attr(self, papa, mama, deda, baba):
        self.papa = papa
        self.mama = mama
        self.deda = deda
        self.baba = baba
        self.count_money = papa + mama + deda + baba

    def check_money(self):
        if self.count_money < 80:
            print("Денег не хватает")
        else:
            print("Ура, денег хватает!")


masha = NewJournal()
masha.set_attr(10, 20, 30, 40)
masha.check_money()


# Часть кода уже есть, заполните оставшуюся часть по заданию.
# Создайте метод count_distance с параметрами (self, point1, point2). Метод принимает названия городов (point1, point2), и вычисляет расстояние между ними. Если такого города среди атрибутов нет, выводит сообщение:
# Извините, программа ещё в разработке.
# Для подсчётов сделайте в методе count_distance вот что:
# - Если point1 == point2, выведите на экран число 0.
# - Иначе, создайте цикл:
#         - С помощь цикла for пройдитесь по списку с атрибутами [self.distance1, self.distance2, self.distance3].
#         - Если point1 и point2 находятся в атрибуте, то выведите на экран расстояние, указанное в этом атрибуте.
#           Например, если point1 и point2 в атрибуте self.distance1 нужно вывести 1860 и завершить цикл вызвав break.
#         - Если ни одно условие в цикле не выполнится, нужно вывести на экран сообщение:
#           "Извините, программа ещё в разработке". Для этого используйте else.
#           Напомню, else в цикле выполняется всегда в конце всех итераций, если в цикле не активировался break.


class GPS:
    distance1 = ("Москва", "Екатеринбург", 1860)
    distance2 = ("Москва", "Казань", 840)
    distance3 = ("Москва", "Нижний Новгород", 430)

    def count_distance(self, point1, point2):
        if point1 == point2:
            print(0)
        else:
            for city in [self.distance1, self.distance2, self.distance3]:
                if point1 in city and point2 in city:
                    print(city[2])
                    break
            else:
                print("Извините, программа ещё в разработке")


dis1 = GPS()
dis2 = GPS()
dis3 = GPS()

dis1.count_distance("Москва", "Казань")
dis2.count_distance("Екатеринбург", "Москва")
dis2.count_distance("Казань", "Казань")
dis3.count_distance("Нижний Новгород", "Екатеринбург")
