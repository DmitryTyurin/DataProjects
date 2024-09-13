# Перед вами декоратор uppercase , который преобразует к заглавному регистру все буквы результата оригинальной функции
# Ваша задача задекорировать функцию calculate_tax декоратором uppercase, чтобы в трех принтах мы уже увидели результат задекорированной функции.


def uppercase(func):
    def inner(n, i, rate):
        res = func(n, i, rate)
        return res.upper()

    return inner


# Задекорируйте функцию calculate_tax
@uppercase
def calculate_tax(name, income, tax_rate):
    tax = income - income * (1 - tax_rate / 100)
    return f"{name} должен заплатить налог {tax}$"


print(calculate_tax("Ivan", 5000, 25))
print(calculate_tax("vaSilIy", 15000, 30))
print(calculate_tax("depardieu", 215000, 40))


# Программист Кузьма познакомился с декораторами и решил написать свой первый пример, где он пытался сопроводить вызов функции add дополнительными выводами на экран. Вот что получилось:
def decorator(func):
    def wrapper(*args, **kwargs):
        print("---Start calculation---")
        result = func(*args, **kwargs)
        print(f"---Finish calculation. Result is {result}---")
        return result

    return wrapper


@decorator
def add(a, b):
    return a + b


# Теперь убедитесь, что декоратор Кузьмы из предыдущего задания успешно работает и с другими функциями, вне зависимости от количества аргументов и их типов.
# Для решения задачи вам необходимо написать только определение функции-декоратора decorator.
def decorator(func):
    def wrapper(*args, **kwargs):
        print("---Start calculation---")
        result = func(*args, **kwargs)
        print(f"---Finish calculation. Result is {result}---")
        return result

    return wrapper
