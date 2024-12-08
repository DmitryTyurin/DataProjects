# Напишите программу, которая считает сумму двух чисел.

print(sum(list(map(int, input().split()))))


# В программу вводится скорость автомобиля в n км/ч, и требуется вычислить расстояние,
# которое он сможет проехать за x часов.
# На вход подается строка чисел, разделенных пробелами, где первое число — это n, а второе — x.

s, t = map(int, input().split())

print(s * t)


# Напишите программу, которая проверяет, равна ли сумма первых двух цифр четырёхзначного числа сумме последних двух цифр.
# На вход программе подается число.
# Программа должна выводить True, если сумма первых двух цифр равна сумме последних двух, и False в противном случае.


def check_sum(num: int) -> bool:
    num_str = str(num)

    if len(num_str) != 4:
        return False

    first_sum = int(num_str[0]) + int(num_str[1])
    last_sum = int(num_str[2]) + int(num_str[3])

    return first_sum == last_sum


print(check_sum(int(input())))


# Гипотеза Коллатца утверждает, что независимо от начального числа n вы рано или поздно придёте в число 1
# , которое находится в цикле [1,4,2,1].
# Предлагаем вам проверить данное утверждение — начиная с числа n ,
# выводите все числа в последовательности, пока не доберётесь до 1.
#
# n / 2 - если n четное
# 3⋅n+1, если n — нечётное.


def collatz(n: int) -> None:
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(n)


collatz(int(input()))


# Существует старинное поверье, утверждающее, что трёхзначное число считается красивым, если сумма его наименьшей и
# наибольшей цифры равна квадрату оставшейся цифры. Выведите True если это так, иначе False


def func(num: int) -> bool:
    num_str = str(num)

    if len(num_str) != 3:
        return False

    min_digit = min(num_str)
    max_digit = max(num_str)

    remaining_digit = str(int(num_str.replace(min_digit, "").replace(max_digit, "")))

    return int(min_digit) + int(max_digit) == int(remaining_digit) ** 2


print(func(int(input())))


# Существует древнее поверье, согласно которому число считается красивым, если первая и последняя цифры — простые числа,
# а все остальные цифры — составные. Выведите True, если это так, иначе — False.


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** (0.5)) + 1):
        if n % i == 0:
            return False
    return True


def is_composite(n):
    return not is_prime(n)


def is_beautiful_number(num):
    digits = list(map(int, str(num)))

    if not (is_prime(digits[0]) and is_prime(digits[-1])):
        return False

    for digit in digits[1:-1]:
        if is_prime(digit):
            return False

    return True


num = int(input())
print(is_beautiful_number(num))
