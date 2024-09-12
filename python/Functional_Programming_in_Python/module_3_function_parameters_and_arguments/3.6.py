# Почините программу, чтобы функция print_values смогла отработать и вывести приветствия на экран


def print_values(one, two, three):
    print(one, two, three)


words = "Hello", "Aloha", "Bonjour"
print_values(*words)


# Напишите функцию count_args, которая принимает произвольное количество аргументов. Данная функция должна возвращать количество переданных ей на вход аргументов
#
# Вам необходимо написать только определение функции count_args


def count_args(*args):
    return len(args)


# Напишите функцию multiply, которая принимает произвольное количество числовых аргументов. Данная функция должна находить произведение всех переданных значений и возвращать его в качестве результата
#
# При вызове multiply без параметров должен возвращаться результат 1.
#
# Вам необходимо написать только определение функции multiply


def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result


# Напишите функцию check_sum, которая принимает произвольное количество аргументов типа int.
#
# Данная функция должна вывести на экран фразу «not enough», если сумма всех элементов меньше 50, в противном случае нужно вывести «verification passed»
#
# Вам необходимо написать только определение функции check_sum
def check_sum(*args):
    if sum(args) < 50:
        print("not enough")
    else:
        print("verification passed")


# Напишите функцию is_only_one_positive, которая принимает произвольное количество числовых аргументов и возвращает True, когда из всех переданных значений только одно положительное, в противном случае верните False
#
# Вам необходимо написать только определение функции is_only_one_positive
def is_only_one_positive(*args):
    positive_count = sum(1 for num in args if num > 0)
    return positive_count == 1


# Давайте теперь создадим функцию print_goods, которая печатает список покупок. На вход она будет принимать произвольное количество значений, а товаром мы будем считать любые непустые строки. Следовательно все числа, списки, словари и другие нестроковые объекты вам нужно будет проигнорировать.
#
# Функция print_goods должна печатать список товаров в виде: «<Порядковый номер товара>. <Название товара>». На примерах ниже вы можете посмотреть как должна работать функция print_goods
#
# print_goods('apple', 'banana', 'orange')
# # Программа должна вывести следующее:
# 1. apple
# 2. banana
# 3. orange
#
# print_goods(1, True, 'Грушечка', '', 'Pineapple')
# # Программа должна вывести следующее:
# 1. Грушечка
# 2. Pineapple
# В случае, если среди переданных значений не встретится ни одного товара, необходимо распечатать фразу «Нет товаров»
#
# print_goods([], {}, 1, 2)
# # Программа должна вывести следующее:
# Нет товаров
# Вам необходимо написать только определение функции print_goods


def print_goods(*args):
    goods = [arg for arg in args if isinstance(arg, str) and arg]
    if goods:
        for i, good in enumerate(goods, 1):
            print(f"{i}. {good}")
    else:
        print("Нет товаров")