# Перепишите код ниже так, чтобы напротив результата вызова функции выводилось значение, хранящееся по ключу
def red():
    return "Color is red"


def green():
    return "Color is green"


def blue():
    return f"Color is blue"


colors = {}
colors[green] = "00FF00"
colors[blue] = "0000FF"
colors[red] = "FF0000"

for i in colors:
    print(f"{i()} - {colors[i]}")


# Представь, что ты работаешь в компании, которая занимается разработкой программного обеспечения. Твой начальник дал тебе задание написать программу, которая будет вычислять факториал числа. Факториал числа - это произведение всех натуральных чисел от 1 до этого числа. Например, факториал числа 5 равен 1 * 2 * 3 * 4 * 5 = 120.
#
# Однако, есть одно условие: ты должен сохранить результат вычисления факториала в глобальной переменной, чтобы его можно было использовать в других частях программы. Это означает, что значение факториала будет доступно для использования в других функциях или блоках кода.
#
# Также, твой начальник хочет, чтобы программа была оптимизирована и не вычисляла факториал числа каждый раз заново. Вместо этого, программа должна проверять, вызывалась ли уже функция с таким параметром. Если функция уже вызывалась с таким параметром, то программа должна вернуть сохраненное значение, а не вычислять его заново. Также перед возвратом такого значения функция должна вывести на экран «Get from cache value factorial(n)»
#
# Таким образом, твоя задача - написать функцию factorial, которая будет вычислять факториал числа, сохранять результат в глобальной переменной и проверять, вызывалась ли уже функция с таким параметром.


def factorial(n):
    global factorial_cache
    if factorial_cache is None:
        factorial_cache = {}

    if n in factorial_cache:
        print(f"Get from cache value factorial({n})")
        return factorial_cache[n]

    result = 1
    for i in range(1, n + 1):
        result *= i

    factorial_cache[n] = result
    return result


factorial_cache = None