# Создайте класс.
# Создайте метод класса. В скобках метода укажите три параметра: (cls, x, y).
# Метод создаёт атрибуты x и y в классе, со значениями параметров x и y соответственно. Например cls.x = x.
# Метод также выполняет умножение x на y, и выводит на экран результат с помощью print().
# Вызовите метод через класс, и укажите в аргументах число 5 и 20. Например Класс.метод(5, 20). При вызове не нужно использовать print.


class MyFirstClass:
    @classmethod
    def multiplication(cls, x, y):
        cls.x = x
        cls.y = y

        print(cls.x * cls.y)


MyFirstClass.multiplication(5, 20)


# Создайте класс Counter.
# Создайте в классе атрибут count равный нулю.
# Создайте два метода: add_count и set_zero. Оба метода являются методами класса.
# Метод add_count() использует параметр по умолчанию add=1, и изменяет атрибут класса count, добавляя к его значению число add. Изначально он добавляет 1, но при желании можно изменить это число. Например, Counter.add_count(5) добавит к значению count число 5, а Counter.add_count() добавит 1.
# Метод  set_zero() изменяет значение атрибута класса count на 0. То есть сбрасывает счётчик.
# Часть кода уже есть. Вам нужно лишь выполнить то, что написано в задании.


class Counter:
    count = 0

    @classmethod
    def add_count(cls, add=1):
        cls.count += add

    @classmethod
    def set_zero(cls):
        cls.count = 0


Counter.add_count()
Counter.set_zero()
Counter.add_count(110)
Counter.add_count()
print(Counter.count)


# Создайте класс MagicBank и объявите внутри класса атрибут money = 1000.
# Создайте метод класса add_money(cls). Метод изменяет значение атрибута класса money, и делает его равным 1000. Затем выводит на экран текст: Ваш счёт снова равен 1000. В print() используйте end='\n\n'.
# Создайте метод класса reduce_money(cls, amount). С помощью этого метода мы осуществляем проверку, покупку и магическое пополнение. Параметр amount - это сумма покупки. Мы не можем осуществить покупку больше чем на 1000 за один раз, поэтому сделайте в методе вот что:
# - Если amount больше 1000, выведите на экран текст: Нельзя тратить больше 1000 за один раз
# - Иначе, выведите на экран: Покупка на сумму amount осуществлена. Например, "Покупка на сумму 500 осуществлена".
# - Теперь нам нужно магически сделать наш счёт равным 1000. Для этого, вызываем метод  add_money() в блоке иначе. Сделать это можно с помощью cls.add_money().


class MagicBank:
    money = 1000

    @classmethod
    def add_money(cls):
        cls.money = 1000
        print(f"Ваш счёт снова равен {cls.money}\n")

    @classmethod
    def reduce_money(cls, amount):
        cls.amount = amount

        if amount > 1000:
            print("Нельзя тратить больше 1000 за один раз")
        else:
            print(f"Покупка на сумму {amount} осуществлена")

            cls.add_money()


masha = MagicBank()
masha.reduce_money(100)
masha.reduce_money(999)
masha.reduce_money(1000000000)


# Создайте класс Time
# Создайте статический метод с помощью декоратора @staticmethod, и назовите его count_time. В параметрах укажите (distance, speed).
# Внутри метода лишь одна операция, подсчёт времени по формуле (time = distance / speed). Метод возвращает результат time с помощью return
# Вызовете метод count_time() через класс, и укажите в аргументах (500, 100). Вызывать нужно через print(), так как метод использует return.


class Time:
    @staticmethod
    def count_time(distance: int, speed: int) -> float | int:
        time = distance / speed

        return time


print(Time.count_time(500, 100))


# Создайте класс Driver
# Объявите статический метод calculate_fuel_costs() с параметрами (distance, fuel, price). Напоминашка: @staticmethod.
# - Создайте переменную result, в ней будет хранится результат подсчётов.
# - Готовая формула подсчётов будет в комментариях.
# - Выведите на экран округлённое значение result, используя функцию round(). Значение округлите до сотых. Постарайтесь сделать округление имено с round(), иначе ответы могут не совпасть.
# Оставшаяся часть кода уже написана, вам нужно сделать то, что указано в задании.


class Driver:

    @staticmethod
    def calculate_fuel_costs(distance, fuel, price):
        result = price * (fuel / 100) * distance
        result = round(result, 2)

        print(result)


vasya = Driver()
vasya.calculate_fuel_costs(3, 7, 50)
vasya.calculate_fuel_costs(100, 7, 50)
vasya.calculate_fuel_costs(50, 7, 50)

# Часть кода уже написана. Для выполнения задания, уже импортирована библиотека datetime. С помощью этой библиотеки мы создадим сегодняшнюю дату (start) и дату окончания (finish). И после этого, мы сможем сравнивать эти даты на "больше, меньше, равно", как обычные числа.
# Создайте класс Product.
# Создайте статический метод check_date(today, expiry). Параметр today - это сегодняшняя дата, а параметр expiry - дата срока годности товара.
# В методе создадим две переменные start и finish:
# start = datetime.strptime(today, "%Y-%m-%d")
# finish = datetime.strptime(expiry, "%Y-%m-%d")
# Сравните finish и start. Если finish больше чем start выведите текст: Срок годности в порядке.
# Иначе выведите текст: Срок годности истёк.
# Вам нужно только сделать то, что в задании, остальное уже готово.

from datetime import datetime


class Product:
    @staticmethod
    def check_date(today, expiry):
        start = datetime.strptime(today, "%Y-%m-%d")
        finish = datetime.strptime(expiry, "%Y-%m-%d")

        if finish > start:
            print("Срок годности в порядке")
        else:
            print("Срок годности истёк")


today_date = "2024-01-12"
expiry_date1 = "2024-01-31"
expiry_date2 = "2024-01-1"
expiry_date3 = "2024-01-12"

Product.check_date(today_date, expiry_date1)
Product.check_date(today_date, expiry_date2)
Product.check_date(today_date, expiry_date3)
