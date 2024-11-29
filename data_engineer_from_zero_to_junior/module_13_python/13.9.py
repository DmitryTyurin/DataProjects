# Напишите функцию count_vowels_consonants(s: str) -> dict, которая принимает строку и возвращает словарь с количеством гласных и согласных.


def count_vowels_consonants(s: str) -> dict:
    s = s.lower()
    count = {"vowels": 0, "consonants": 0}

    for char in s:
        if char.isalpha():
            if char in "aeiou":
                count["vowels"] += 1
            else:
                count["consonants"] += 1

    return count


print(count_vowels_consonants(input()))


# Напишите функцию convert_temperature(temp: float, from_scale: str, to_scale: str) -> float,
# которая конвертирует температуру между шкалами Цельсия, Фаренгейта и Кельвина.


def convert_temperature(temp: float, from_scale: str, to_scale: str) -> float:
    if from_scale == "C":
        temp_in_kelvin = temp + 273.15
    elif from_scale == "F":
        temp_in_kelvin = (temp - 32) * 5 / 9 + 273.15
    else:
        temp_in_kelvin = temp

    if to_scale == "C":
        return temp_in_kelvin - 273.15
    elif to_scale == "F":
        return (temp_in_kelvin - 273.15) * 9 / 5 + 32
    else:
        return temp_in_kelvin


temp, from_scale, to_scale = list(map(str, input().split(", ")))

temp = float(temp)
from_scale = str(from_scale).replace('"', "")
to_scale = str(to_scale).replace('"', "")


print(convert_temperature(float(temp), from_scale, to_scale))


# Напишите функцию second_largest(numbers: list) -> int, которая возвращает второе по величине число в списке.
# Предполагается, что в списке содержится не менее двух уникальных чисел.


def second_largest(numbers: list) -> int:
    sorted_numbers = sorted(numbers, reverse=True)

    return sorted_numbers[1]


print(second_largest([1, 3, 4, 5, 0, 2]))


# Создайте функцию int_to_roman(num: int) -> str, которая переводит целое число (до 3999) в римское представление.

roman_numerals = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}


def int_to_roman(num: int) -> str:
    roman = ""

    for key, value in roman_numerals.items():
        while num >= value:
            roman += key
            num -= value

    return roman


print(int_to_roman(int(input())))


# Создайте функцию reverse_numbers(lst: list) -> list,
# которая принимает список чисел и возвращает новый список, в котором каждое число представлено в обратном порядке.


def reverse_numbers(lst: list) -> list:
    reversed_list = []

    for number in lst:
        reversed_number = int(str(number)[::-1])
        reversed_list.append(reversed_number)

    return reversed_list


print(reverse_numbers([123, 456, 789]))


# Создайте функцию count_divisors(n: int) -> int, которая возвращает количество делителей числа n.
# В примере 6 - потому что делители: 1, 2, 4, 7, 14, 28


def count_divisors(n: int) -> int:
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


print(count_divisors(28))


# Создайте функцию is_balanced_parentheses(s: str) -> bool,
# которая проверяет, сбалансированы ли скобки в строке (каждая открывающая скобка имеет соответствующую закрывающую).


def is_balanced_parentheses(s: str) -> bool:

    stack = []

    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return False
            if char == ")" and stack[-1] != "(":
                return False
            if char == "]" and stack[-1] != "[":
                return False
            if char == "}" and stack[-1] != "{":
                return False
            stack.pop()
    if stack:
        return False

    return True


print(is_balanced_parentheses("( [ { } ] )"))


# Создайте функцию is_almost_palindrome(s: str) -> bool,
# которая проверяет, является ли строка "почти палиндромом" (можно удалить один символ, чтобы она стала палиндромом).


def is_palindrome(s):
    return s == s[::-1]


def is_almost_palindrome(s: str) -> bool:
    for i in range(len(s)):
        new_s = s[:i] + s[i + 1 :]
        if is_palindrome(new_s):
            return True
    return False


print(is_almost_palindrome(input()))
