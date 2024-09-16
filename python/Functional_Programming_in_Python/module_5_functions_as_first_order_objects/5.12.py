# Создайте декоратор multiply_result_by, который принимает аргумент N и возвращает функцию-декоратор, которая умножает результат декорированной функции на N
def multiply_result_by(N):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * N

        return wrapper

    return decorator


# Ваша задача переписать декоратор limit_query так, чтобы он ограничивал разрешенное количество вызовов оригинальной функции по переданному параметру limit. Когда декорируемая функция исчерпает лимит вызовов, необходимо выводить на экран фразу
#  «Лимит вызовов закончен, все <limit> попытки израсходованы»
# Если лимит исчерпан, оригинальная функция не должна быть вызвана, декоратор возвращает None


def limit_query(limit):
    def decorator(func):
        def add(*args, **kwargs):
            if add.counter >= limit:
                print(f"Лимит вызовов закончен, все {limit} попытки израсходованы")
                return None
            add.counter += 1
            return func(*args, **kwargs)

        add.counter = 0
        return add

    return decorator


# Напишите декоратор convert_to, который позволяет автоматически преобразовать возвращаемое значение в указанный тип данных. Функция-декоратор convert_to имеет обязательный параметр type_, в который необходимо передать тип данных для дальнейшего преобразования.


def convert_to(type_):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return type_(result)

        return wrapper

    return decorator


# Помните декоратор validate_all_args_str, который проверял, что все переданные позиционные значения являются строками? А если вдруг нам потребуется создать декоратор, который будет проверять аргументы не на принадлежность к строке, а, скажем, к списку или числу? Тогда нам понадобится создавать отдельный декоратор на каждый тип данных. Или сделать параметризированный декоратор validate_all_args, который будет принимать тип данных в качестве аргумента и проверять, что все значения в args относятся к переданному типу данных.
#
# Ваша задача написать такой декоратор validate_all_args, который имеет параметр type_. Если все позиционные аргументы принадлежат типу type_, то запускается оригинальная функция; в противном случае необходимо отменить ее запуск и вывести сообщение
#
# Все аргументы должны принадлежать типу {type_}


def validate_all_args(type_):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not all(isinstance(arg, type_) for arg in args):
                print(f"Все аргументы должны принадлежать типу {type_}")
                return None
            return func(*args, **kwargs)

        return wrapper

    return decorator


# Ваша задача написать параметризированный декоратор compose, который принимает произвольное количество функций и применяет их последовательно к результату декорируемой функции

from functools import reduce


def compose(*functions):
    def decorator(function):
        def wrapper(*args, **kwargs):
            composed_function = reduce(
                lambda f, g: lambda *args, **kwargs: g(f(*args, **kwargs)),
                functions,
                function,
            )
            return composed_function(*args, **kwargs)

        return wrapper

    return decorator


# Ваша задача написать параметризированный декоратор add_attrs, который принимает произвольное количество именованных аргументов и на их основании добавляет новые атрибуты для оригинальной функции
def add_attrs(**attrs):
    def decorator(func):
        for attr_name, attr_value in attrs.items():
            setattr(func, attr_name, attr_value)
        return func

    return decorator


# Ваша задача переписать декоратор monkey_patching. Ранее он заменял значения всех переданных аргументов при вызове оригинальной функции следующим образом:
#
#     ➕   значение каждого позиционного аргумента заменяется на строку «Monkey»
#
#     ➕   значение каждого именованного аргумента заменяется на строку «patching»
#
# Теперь необходимо завести параметры arg и kwarg, при помощи которых можно влиять на значения, которые будут проставляться в позиционные и именованные аргументы. Параметры arg и kwarg являются необязательными для передачи, их значения по умолчанию «Monkey» и «patching» соответственно.
def monkey_patching(arg="Monkey", kwarg="patching"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            args = list(args)
            for i in range(len(args)):
                args[i] = arg
            for key in kwargs:
                kwargs[key] = kwarg
            return func(*args, **kwargs)

        return wrapper

    return decorator


# Ваша задача написать параметризированный декоратор pass_arguments, который принимает произвольное количество именованных и позиционных аргументов и пробрасывает их дополнительно к аргументам, которые передаются при вызове оригинальной функции
def pass_arguments(*positional_args, **named_args):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if named_args:
                kwargs.update(named_args)
            if positional_args:
                args = positional_args + args
            return func(*args, **kwargs)

        return wrapper

    return decorator
