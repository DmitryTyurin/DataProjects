# Создайте класс BeautyTransform и два метода: __init__() и transformer().
# Метод __init__() имеет два параметра: height и weight=0, и создаёт два атрибута height и weight с этими же значениями. Параметр weight=0 - это параметр по умолчанию, равный нулю.
# Метод transformer(self) содержит внутри конструкцию try-except.
# В блоке try происходит две операции:
# - Создаётся атрибут new_body равный делению self.height / self.weight
# - С помощью print() выводится на экран сообщение: Успешная трансформация ​​​​​​
# Блок except проверяет код на ошибку ZeroDivisionError, и если она обнаружится, выводит на экран текст:
# Лицо как в картине Крик, Эдварда Мунка
# Часть кода уже написана, вам нужно лишь сделать то, что написано выше.


class BeautyTransform:
    def __init__(self, height, weight=0):
        self.height = height
        self.weight = weight

    def transformer(self):
        try:
            new_body = self.height / self.weight
            print("Успешная трансформация")
        except ZeroDivisionError:
            print("Лицо как в картине Крик, Эдварда Мунка")


vasya = BeautyTransform(172, 70)
nastya = BeautyTransform(100, 50)
lena = BeautyTransform(50)

vasya.transformer()
nastya.transformer()
lena.transformer()


# Создайте класс BeautyTransform и два метода: __init__, transformer.
# Метод __init__ имеет два параметра: height, weight и создаёт два атрибута height, weight со значениями параметров height, weight соответственно. Также, __init__ создаёт атрибут result = "Божественная красота".
# Метод transformer(self) содержит внутри конструкцию try-except-else-finally:
# - В блоке try cоздаётся атрибут new_body равный делению self.height / self.weight
# - Блок except проверяет код на разные ошибки, поэтому применяется except Exception. Если ошибка обнаружится, атрибут result получает новое значение: "Индюк на три дня"
# - Блок else выводит сообщение на экран: Проверка прошла! В print() также используется end=' '
# - Блок finally выводит сообщение на экран: Результат: result. Где result - это значение атрибута result.
# Часть кода уже написана, вам нужно лишь сделать задание выше.


class BeautyTransform:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.result = "Божественная красота"

    def transformer(self):
        try:
            self.new_body = self.height / self.weight
        except Exception:
            self.result = "Индюк на три дня"
        else:
            print("Проверка прошла!", end=" ")
        finally:
            print(f"Результат: {self.result}")


nastya = BeautyTransform(100, 50)
lena = BeautyTransform(50, 90)
vasya = BeautyTransform(172, "Индюк")

nastya.transformer()
lena.transformer()
vasya.transformer()
