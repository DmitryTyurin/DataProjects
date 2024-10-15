# Часть кода уже написана.
# Выведите на экран __dict__ экземпляра my с помощью print.


class MyClass:
    name = "Vasya"


my = MyClass()
my.name = "Masha"

print(my.__dict__)

# {'id_1':'Masha', 'id_2':'Tom Cruise', 'id_3':'Nicole Kidman', 'id_4':'Brad Pitt', 'id_5':'Tom Hanks', 'id_6':'Johnny Depp'}
# Задание:
# Часть кода уже готова.
# Вам нужно добавить в экземпляр vasya, 6 атрибутов с именами id_1, id_2 ... id_6, а значения атрибутов будут имена людей из словаря Васи.
# Задание можно сделать разными способами, проявите свои знания на практике. Вам нужно лишь выполнить то, что в задании, остальное уже готово.


friends = {
    "id_1": "Masha",
    "id_2": "Tom Cruise",
    "id_3": "Nicole Kidman",
    "id_4": "Brad Pitt",
    "id_5": "Tom Hanks",
    "id_6": "Johnny Depp",
}


class Person:
    pass


vasya = Person()

vasya.__dict__.update(friends)

for key, value in vasya.__dict__.items():
    print(key, value)


# Часть кода уже написана.
# Выведите на экран, значения всех атрибутов экземпляра person1. Каждое значение должно быть на отдельной строчке.
# Можете сделать простым способом, а можете попробовать через цикл, в любом случае используйте __dict__.


class Person:
    pass


person_1 = Person()
person_1.__dict__ = {"name": "Vasya", "age": "20", "work": "driver"}

for key, value in person_1.__dict__.items():
    print(value)
