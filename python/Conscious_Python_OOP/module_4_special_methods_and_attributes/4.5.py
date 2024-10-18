# Часть кода уже написана.
# Переменная input_word принимает разные строки.
# Напишите ваш код в методе __str__, чтобы команда print(person) выводила сообщение "Да здравствует input_word!". Естественно input_word здесь переменная, и будет принимать разные слова. Пример результатов ниже.


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Да здравствует {self.name}!"


input_word = input()
person = Person(input_word)
print(person)


# Создайте класс, нужные методы, атрибуты и экземпляр. Затем, выведите на экран информацию об экземпляре для программистов. Пример вывода написан ниже (Sample Output). Используйте информацию из примера, чтобы написать код.
class Car:
    def __init__(self):
        self.model = "toyota corolla"
        self.color = "black"
        self.year = 2023

    def __str__(self):
        return f"Класс: {self.__class__.__name__}, Атрибуты экземпляра: {self.__dict__}"


car = Car()
print(car)


# Сделайте так, чтобы экземпляры, с одинаковыми атрибутами и значениями, имели одинаковый хэш.


class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def __hash__(self):
        return hash((self.model, self.color))


car1 = Car("toyota corolla", "black")
car2 = Car("toyota corolla", "black")
print(hash(car1) == hash(car2))
