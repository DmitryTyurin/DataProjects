# На вход программе подается строка чисел, верните массив квадратов каждого числа,
# отсортированного в неубывающем порядке


def sorted_squares(nums: str) -> list[int]:
    nums = list(map(int, nums.split()))

    squares = [num**2 for num in nums]

    squares.sort()

    return squares


print(sorted_squares(input()))


# Выведите, сколькими различными способами можно набрать сумму c, используя только монеты номиналами a и b
# Два способа являются различными, если различается количество монет a в данных способах.
# В первой строке содержится целое число a (1≤a≤100)
# Во второй строке содержится целое число b (1≤b≤100)
# В третьей строке содержится целое число c (1≤c≤106)
# Выходные данные
# В единственной строке выведите целое число — количество способов, которыми можно набрать сумму c,
# используя только монеты номиналами a и b.


def count_ways(a, b, c):
    ways = 0
    max_x = c // a
    for x in range(max_x + 1):
        remainder = c - a * x
        if remainder % b == 0:
            ways += 1
    return ways


a = int(input())
b = int(input())
c = int(input())

result = count_ways(a, b, c)

print(result)


# На вход программе подается число n, нужно возвести число 5 в степень n и узнать последние две цифры числа.
# Входные данные
# Единственная строка входных данных содержит одно целое число n (2 ≤ n ≤ 2·1018) — степень, в которую вам нужно возвести число 5.


def last_two_digits_of_power_5(n: int) -> int:
    if n >= 40:
        return 25
    else:
        return pow(5, n, 100)


n = int(input())

print(last_two_digits_of_power_5(n))


# На вход программе подается целое число n, нужно перевести число в 7 систему счисления и вывести на экран.
# Входные данные
# Единственная строка входных данных содержит одно целое число n (-10^3 <= n <= 10^3)


n = int(input())


if n == 0:
    print(0)
else:

    abs_n = abs(n)

    seven_base_representation = []
    while abs_n > 0:
        seven_base_representation.append(str(abs_n % 7))
        abs_n //= 7
    result = "".join(seven_base_representation[::-1])

    if n < 0:
        result = "-" + result
    print(result)


# На вход программе поступает число n, посчитайте сумму чисел от 1 до n ( включительно ) и выведите на экран.
# Для примера вычислим сумму из первого теста, где n = 7
# 1 + 2 + 3 + 4 + 5 + 6 + 7 получим 28


def sum_from_1_to_n_formula(n):
    return n * (n + 1) // 2


n = int(input())

print(sum_from_1_to_n_formula(n))


# На вход программе подается два числа x и n, каждое на отдельной строке
# Реализуйте pow(x, n) , который вычисляет x возведенную в степень  n (т.е. xn).
# Пример 1:
# Ввод:  x = 3, n = 3.
# Выход: 27


def power(x: int, y: int) -> int:
    if y == 0:
        return 1

    if y > 0:
        result = 1
        for _ in range(y):
            result *= x
        return result

    else:
        result = 1
        for _ in range(-y):
            result *= x
        return 1 / result


x, y = int(input()), int(input())

print(power(x, y))
