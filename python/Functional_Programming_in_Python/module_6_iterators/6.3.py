# Напишите функцию filter_numbers, которая принимает список целых чисел и возвращает новый список, который
# состоит только из четных чисел входного списка или из тех, которые по модулю больше 100.


def filter_numbers(numbers: list[int]) -> list[int]:
    return list(filter(lambda x: x % 2 == 0 or abs(x) > 100, numbers))


# Напишите функцию filter_words, которая принимает список строк и возвращает новый список, который состоит из строк,
# длина которых четыре символа, или начинающихся на заглавную букву S.

filter_words = lambda words: list(filter(lambda x: len(x) == 4 or x[0] == "S", words))
words = [
    "scheme",
    "hypnothize",
    "exposure",
    "Syndrome",
    "Save",
    "speculate",
    "cane",
    "welfare",
    "blame",
    "core",
]
print(filter_words(words))


# Ваша задачи — избавиться от циклов for при помощи map и filter.
# Для этого перепишите функцию get_values, но так, чтобы она не меняла свою изначальную функциональность
def get_values(nums: tuple[int, ...]) -> tuple[int, ...]:
    lst = list(filter(lambda x: x % 3 == 0, nums))
    lst = tuple(map(lambda x: x * 3, lst))

    return lst

# Напишите функцию filter_tuples, которая принимает кортеж кортежей из трех числовых значений.
# Функция filter_tuples должна вернуть новый кортеж, который состоит только из тех элементов входного кортежа, произведение значений которых равно 60
def filter_tuples(tuples: tuple[tuple[int, int, int], ...]) -> tuple[tuple[int, int, int], ...]:
    return tuple(filter(lambda x: x[0] * x[1] * x[2] == 60, tuples))

# Перед вами список словарей foods, который хранит в себе информацию о меню ресторана. Проанализируйте ключи и значения, хранящиеся в словарях списка foods, они вам потребуются для задания.
# Ваша задача — найти все имена блюд, которые являются  салатами в списке foods. Из имен салатов необходимо составить список, элементы которого должны следовать в том же порядке, как и в списке foods.
# В качестве ответа выведите на экран найденный список.
# Используйте функции map и filter.

foods = [
    {'name': "Стейк Рибай", 'type_food': "Основное", 'price': 75.95},
    {'name': "Ассорти из гигантских креветок", 'type_food': "Закуска", 'price': 2029.95},
    {'name': "Оливье", 'type_food': "Салат", 'price': 329.95},
    {'name': "Жареный канадский бекон", 'type_food': "Закуска", 'price': 239.95},
    {'name': "Крабовый пирог", 'type_food': "Закуска", 'price': 532.95},
    {'name': "Цезарь", 'type_food': "Салат", 'price': 14.95},
    {'name': "Пирог из лобстера", 'type_food': "Закуска", 'price': 230.95},
    {'name': "Огурчики", 'type_food': "Закуска", 'price': 123.95},
    {'name': "Мимоза", 'type_food': "Салат", 'price': 223.95},
    {'name': "Овощной", 'type_food': "Салат", 'price': 310.95},
    {'name': "Картошка фри", 'type_food': "Гарнир", 'price': 234.95},
    {'name': "Спаржа", 'type_food': "Гарнир", 'price': 455.95},
    {'name': "Стейк Техасский", 'type_food': "Основное", 'price': 1631.95},
    {'name': "Грибы", 'type_food': "Гарнир", 'price': 234.95},
    {'name': "Лосось на гриле", 'type_food': "Основное", 'price': 936.95},
    {'name': "Крабовый", 'type_food': "Салат", 'price': 563.95}
]

def get_names(foods: list[dict[str, str]]) -> list[str]:
    return list(map(lambda x: x['name'], filter(lambda x: x['type_food'] == "Салат", foods)))

# Перед вами вновь список словарей foods
# Ваша задача найти суммарную стоимость всех основных блюд, которые имеются в списке foods
# В качестве ответа выведите найденную сумму, округленную до двух знаков после запятой
def get_sum(foods: list[dict[str, str]]) -> float:
     return round(sum(list(map(lambda x: x['price'], filter(lambda x: x['type_food'] == "Основное", foods)))), 2)
print(get_sum(foods))

