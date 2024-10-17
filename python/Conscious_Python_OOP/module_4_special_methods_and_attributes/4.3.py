# Часть кода уже написана, вам нужно лишь объявить метод __eq__
# Метод __eq__(self, other) содержит две проверки:
# - Если other является экземпляром класса Number, то возвращается результат сравнения (==) атрибутов summa у двух экземпляров класса. То есть self и other здесь являются экземплярами и нужно сравнить атрибуты summa этих экземпляров и вернуть результат.
# - Если other является числом (int), то возвращается результат сравнения (==) атрибута summa , с other.
# - Для проверки лучше всего использовать isinstance().


class Number:
    def __init__(self, x, y):
        self.summa = x + y

    def __eq__(self, other):
        if isinstance(other, Number):
            return self.summa == other.summa
        elif isinstance(other, int):
            return self.summa == other
        else:
            return False


number_1 = Number(4, 2)
number_2 = Number(5, 5)
print(number_1 == number_2)
print(number_1 == 10)
print(number_2 == 10)


# Большая часть кода уже написана. Создайте метод(ы), чтобы результаты сравнения были как в коде.
# Метод(ы) сравнивают длину (len) списков.


class Lists:
    def __init__(self, lists):
        self.lists = lists

    def __lt__(self, other):
        return len(self.lists) < len(other.lists)

    def __gt__(self, other):
        return len(self.lists) > len(other.lists)


# код ниже не меняйте, во имя вселенной
lst1 = Lists(["a", "b", "c"])
lst2 = Lists([1, 2, 3, 4, 5])
print(lst1 < lst2)  # True
print(lst1 > lst2)  # False


# Часть кода уже написана, вам нужно лишь объявить методы __ge__, __le__. Эти методы, сравнивают экземпляры по количеству страниц в книге на ">=" и "<=".


class Books:
    def __init__(self, book_name, book_page):
        self.book_name = book_name
        self.book_page = book_page

    def __ge__(self, other):
        return self.book_page >= other.book_page

    def __le__(self, other):
        return self.book_page <= other.book_page


book1 = Books("Война и мир", 1360)
book2 = Books("Собака Баскервилей", 112)
book3 = Books("Скотный двор", 112)

print(book1 >= book2)
print(book1 >= book3)
print(book2 <= book3)
