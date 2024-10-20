# Создайте класс Bank
# Объявите три метода: __init__, print_balance, change_balance
# Метод __init__ имеет три параметра:  имя клиента, номер карты и баланс, и создаёт три приватных атрибута. Имена параметрам и атрибутам придумайте сами.
# Метод print_balance является обычным методом, и выводит на экран баланс клиента с помощью print().
# Метод change_balance имеет параметр (self, money), и изменяет баланс клиента. Если money отрицательное, то баланс уменьшается, если money положительное, то баланс увеличивается. Метод только изменяет атрибут связанный с балансом.
# Часть кода уже написана, вам нужно лишь сделать то, что написано выше.


class Bank:
    def __init__(self, name, card_number, balance):
        self.__name = name
        self.__card_number = card_number
        self.__balance = balance

    def print_balance(self):
        print(self.__balance)

    def change_balance(self, money):
        self.__balance += money


id_1 = Bank("Vasya", 12345678, 500)
id_1.change_balance(-500)
id_1.print_balance()


# Импортируйте модуль accessify (from accessify import private)
# Создайте класс Teleport
# Создайте приватный метод __activator_teleport(), используя декоратор @private. Метод выводит на экран информацию:
# "Активатор от телепорта у Машеньки под подушкой".
# Создайте публичный метод mama_help(). Метод вызывает приватный метод  __activator_teleport().
# К сожалению, на Stepik нет модуля accessify. Поэтому задание выполните у себя на компьютере, например в PyCharm. Часть кода уже написана, сюда вставьте ваш код из PyCharm, но без импорта модуля и без декоратора. Либо закомментируйте импорт и декоратор. Не забывайте про self и скобки при вызове методов.


class Teleport:
    def __activator_teleport(self):
        print("Активатор от телепорта у Машеньки под подушкой")

    def mama_help(self):
        self.__activator_teleport()


vasya = Teleport()
vasya.mama_help()


# Часть кода уже написана
# Создайте с помощью геттера, сеттера и делиттера, возможность взаимодействовать с атрибутом __balance.
# Геттер возвращает значение баланса.
# Сеттер устанавливает новый баланс.
# Делиттер не удаляет баланс, но меняет его на число 0.
# Посмотрите на код проверки, и подумайте как назвать ваши методы, чтобы всё сработало правильно.
# Вам нужно лишь объявить сеттер, геттер и делиттер, всё остальное уже готово.


class MagicBank:
    def __init__(self, account, balance):
        self.__account = account
        self.__balance = balance

    @property
    def happy_balance(self):
        return self.__balance

    @happy_balance.setter
    def happy_balance(self, balance):
        self.__balance = balance

    @happy_balance.deleter
    def happy_balance(self):
        self.__balance = 0


id_1 = MagicBank("Машенька", 500)
print(id_1.happy_balance)

id_1.happy_balance = 1000
print(id_1.happy_balance)

del id_1.happy_balance
print(id_1.happy_balance)
