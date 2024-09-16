# Отредактируйте код так, чтобы сохранялись оригинальное имя и док строка декорируемой функции
# Сделайте это без использования функции wraps.
def upper(func):
    def inner(*args, **kwargs):
        """
        Внутренняя функция декоратора
        """
        return func(*args, **kwargs).upper()

    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner


# Напишите декоратор limit_query, который ограничивает вызов оригинальной функции так, чтобы она могла вызываться не больше трех раз. Когда декорируемая функция исчерпает лимит вызовов, необходимо выводить на экран фразу
#  «Лимит вызовов закончен, все 3 попытки израсходованы»
# Если лимит исчерпан, оригинальная функция не должна быть вызвана, декоратор возвращает None
def limit_query(func):
    count = 0

    def add(*args, **kwargs):
        nonlocal count
        if count < 3:
            count += 1
            return func(*args, **kwargs)
        else:
            print("Лимит вызовов закончен, все 3 попытки израсходованы")
            return None

    return add


# Напишите декоратор add_args, который добавляет к переданным аргументам еще два значения: строку «begin» в начало аргументов, строку «end» в конец. Также декоратор должен сохранить первоначальное имя декорируемой функции и ее строку документации
def add_args(func):
    def inner(*args, **kwargs):
        args = ("begin", *args, "end")
        return func(*args, **kwargs)

    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner


# Реализуйте декоратор explicit_args, который не позволяет запускать оригинальную функцию, если были переданы позиционные аргументы. Декоратор explicit_args должен выводить фразу
# Вы не можете передать позиционные аргументы. Используйте именованный способ передачи значений
# и предотвращать запуск оригинальной функции


def explicit_args(func):
    def inner(*args, **kwargs):
        if args:
            print(
                "Вы не можете передать позиционные аргументы. Используйте именованный способ передачи значений"
            )
            return None
        return func(*args, **kwargs)

    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner


# Реализуйте декоратор reverse, который сделает так, чтобы декорированная функция принимала все свои позиционные аргументы в обратном порядке. Именованные аргументы должны игнорироваться декоратором reverse.


def reverse(func):
    def inner(*args, **kwargs):
        return func(*args[::-1], **kwargs)

    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner


# Monkey patch -  это прием в программировании, который используется для динамического изменения поведения фрагмента кода во время выполнения.
#
# Ваша задача написать декоратор monkey_patching, который заменяет значения всех переданных аргументов при вызове оригинальной функции следующим образом:
#
#     ➕   значение каждого позиционного аргумента заменяется на строку «Monkey»
#
#     ➕   значение каждого именованного аргумента заменяется на строку «patching»

from functools import wraps


def monkey_patching(func):
    @wraps(func)
    def inner(*args, **kwargs):
        args = tuple("Monkey" for _ in args)
        kwargs = {key: "patching" for key in kwargs}
        return func(*args, **kwargs)

    return inner


# Реализуйте декоратор counting_calls, который будет подсчитывать количество вызовов оригинальной функции.
# После декорирования при помощи counting_calls у функции должен появиться атрибут call_count, который отслеживает текущее количество вызовов.

from functools import wraps


def counting_calls(func):
    @wraps(func)
    def inner(*args, **kwargs):
        inner.call_count += 1
        return func(*args, **kwargs)

    inner.call_count = 0

    return inner


# Усовершенствуем ранее созданный декоратор counting_calls, добавив отслеживание переданных аргументов при каждом вызове.
# Для этого декоратор counting_calls должен добавить в декорируемой функции атрибут calls - список, в который будут сохраняться все переданные аргументы в момент вызова в виде словаря.
# Каждый словарь должен иметь два ключа: args и kwargs для сохранения соответствующих аргументов.

from functools import wraps


def counting_calls(func):
    @wraps(func)
    def inner(*args, **kwargs):
        inner.calls.append({"args": args, "kwargs": kwargs})
        inner.call_count += 1
        return func(*args, **kwargs)

    inner.calls = []
    inner.call_count = 0

    return inner
