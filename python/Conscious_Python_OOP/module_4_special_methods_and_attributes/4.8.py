# Часть кода уже написана.
# Добавьте недостающий код, только в методе __new__.
# В методе __new__ сделайте проверку, если number меньше 1000, то экземпляр не создаётся. Если больше или равно, то экземпляр создастся. Чтобы отменить создание экземпляра, можете использовать pass.


class StopNumber:
    def __new__(cls, number, name):
        cls.number = number
        cls.name = name

        if number < 1000:
            return None
        else:
            return super().__new__(cls)

    def __init__(self, number, name):
        self.number = number
        self.name = name


Masha = StopNumber(500, "Masha")
Vika = StopNumber(1500, "Vika")
Lena = StopNumber(1200, "Lena")

print(isinstance(Masha, StopNumber))
print(isinstance(Vika, StopNumber))
print(isinstance(Lena, StopNumber))


# Часть кода уже написана
# Объявите только метод: __call__ . Метод __call__ имеет один параметр (number) и делает подсчёт, через сколько лет экземпляру будет number лет. В нашем случае, мы будем вставлять число 20. Метод возвращает результат (return).
# Метод __init__ уже выводит результат print(self(20)), поэтому только объявите метод __call__


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self(20))

    def __call__(self, number):
        return number - self.age


masha = Person("Masha", 9)
vasya = Person("Vasya", 19)


# Часть кода уже написана
# Объявите нужные методы, чтобы класс выполнял роль декоратора. Функция с декоратором должна возвращать число в три раза больше, чем число, которое возвращает функция. Например, функция принимает 5 страницы и возвращает 5 страницы, а декоратор делает так, что функция вернёт 15.
# В функции ничего не меняйте, вам нужно лишь объявить нужные методы в классе.


class ReadingAccelerator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs) * 3


@ReadingAccelerator
def masha_reading(page_number):
    return page_number


print(masha_reading(5))
