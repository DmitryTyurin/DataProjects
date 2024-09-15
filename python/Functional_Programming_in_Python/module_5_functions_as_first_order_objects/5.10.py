# Перед вами реализация двух функций-декораторов  first_validator и second_validator.
#
# Также имеется функция sum_values.
#
# Вам необходимо сперва проанализировать имеющийся код и разобраться, как он работает.
#
# После этого вашей задачей является:
#
#    ✔️ наложить два декоратора на функцию sum_values в правильной последовательности;
#
#    ✔️ вызвать задекорированную функцию sum_values подобрав аргументы так, чтобы совпал вывод результата.
#
# Код самих функций менять не нужно.


def first_validator(func):
    def wrapper(*args, **kwargs):
        print(f"Начинаем важную проверку")
        if len(args) == 3:
            func(*args, **kwargs)
        else:
            print(f"Важная проверка не пройдена")
            return None
        print(f"Заканчиваем важную проверку")

    return wrapper


def second_validator(func):
    def wrapper(*args, **kwargs):
        print(f"Начинаем самую важную проверку")
        if kwargs.get("name") == "Boris":
            func(*args)
        else:
            print(f"Самая важная проверка не пройдена")
            return None
        print(f"Заканчиваем самую важную проверку")

    return wrapper


# используйте декораторы
@second_validator
@first_validator
def sum_values(*args):
    print(f"Получили результат равный {sum(args)}")


# Теперь вызываем задекорированную функцию с нужными аргументами
sum_values(60, 7, 10, name="Boris")


# Напишите декоратор validate_all_args_str, который проверяет на корректность (валидирует) переданные позиционные аргументы. Корректным он считает любое строковое значение, стоящее в позиционном аргументе; ключевые аргументы при проверке игнорируются. Если было передано хотя бы одно не строковое значение в позиционный аргумент, функция-декоратор validate_all_args_str должна
#
# вывести на экран фразу «Все аргументы должны быть строками»
# вернуть None и не запускать оригинальную  функцию
# Если же все аргументы корректны, validate_all_args_str запускает оригинальную функцию со всеми переданными значениями.


def validate_all_args_str(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, str):
                print("Все аргументы должны быть строками")
                return None
        return func(*args, **kwargs)

    return wrapper


# Напишите декоратор validate_all_kwargs_int_pos, который проверяет на корректность переданные именованные аргументы. Корректным будет считаться именованный аргумент, значение которого является целым положительным числом. Позиционные аргументы игнорируются во время проверки декоратора validate_all_kwargs_int_pos.
# Если было передано хотя бы одно некорректное значение в именованный аргумент, функция-декоратор validate_all_kwargs_int_pos должна:
# вывести на экран фразу «Все именованные аргументы должны быть положительными числами»;
# вернуть None и не запускать оригинальную  функцию.
# Если же все аргументы корректны, validate_all_kwargs_int_pos запускает оригинальную функцию со всеми переданными значениями.
# Также для проверки вам необходимо скопировать из предыдущего шага реализацию декоратора validate_all_args_str, потому что в проверках будет использоваться валидация сразу и на *args, и на **kwargs.


def validate_all_args_str(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, str):
                print("Все аргументы должны быть строками")
                return None
        return func(*args, **kwargs)

    return wrapper


def validate_all_kwargs_int_pos(func):
    def wrapper(*args, **kwargs):
        for key, value in kwargs.items():
            if not isinstance(value, int) or value <= 0:
                print("Все именованные аргументы должны быть положительными числами")
                return None
        return func(*args, **kwargs)

    return wrapper


# Ваша задача создать два декоратора
#
#     1️⃣ filter_even, который фильтрует только позиционные аргументы. Среди всех переданных значений он оставляет только четные числа, False и коллекции, длина которых четная
#
#     2️⃣ delete_short, который фильтрует только именованные аргументы. Среди всех переданных значений он оставляет только те, имена которых более четырех символов
def filter_even(func):
    def wrapper(*args, **kwargs):
        even_args = [
            arg
            for arg in args
            if isinstance(arg, int)
            and arg % 2 == 0
            or arg is False
            or isinstance(arg, (str, list, tuple, dict))
            and len(arg) % 2 == 0
        ]
        return func(*even_args, **kwargs)

    return wrapper


def delete_short(func):
    def wrapper(*args, **kwargs):
        long_kwargs = {k: v for k, v in kwargs.items() if len(k) > 4}
        return func(*args, **long_kwargs)

    return wrapper


# Напишите декоратор repeater, который трижды вызывает декорированную функцию
# Ваша задача написать только определение функции декоратора repeater


def repeater(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


# Напишите декоратор double_it, который возвращает удвоенный результат вызова декорированной функции
# Ваша задача написать только определение функции декоратора double_it


def double_it(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2

    return wrapper


# Ваша задача написать логику работы декоратора uppercase_elements, который умеет работать с функциями, возвращающими коллекции элементов. Задача декоратора uppercase_elements преобразовать каждый строковый элемент коллекции к заглавному регистру. В случае, если оригинальная функция возвращает словарь, то элементом считаем только строковые ключи словаря.
# Элементы, не являющиеся строкой, не должны изменяться декоратором uppercase_elements
# Гарантируется, что коллекции, возвращаемые оригинальной функцией, не являются вложенными


def uppercase_elements(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, dict):
            new_dict = {}
            for key, value in result.items():
                if isinstance(value, str) and isinstance(key, int):
                    new_dict[key] = value
                else:
                    new_dict[key.upper()] = value
            result = new_dict
        elif isinstance(result, list):
            new_list = []
            for element in result:
                if isinstance(element, str):
                    new_list.append(element.upper())
                else:
                    new_list.append(element)
            result = new_list
        return result

    return wrapper
