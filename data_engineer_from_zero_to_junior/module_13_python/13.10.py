# Напишите функцию rounded_sqrt(n: int) -> int, которая принимает число n и возвращает его квадратный корень,
# округленный до ближайшего целого, с использованием math.sqrt() и math.floor() или math.ceil().

import math


def rounded_sqrt(n: int) -> int:
    sqrt = math.sqrt(n)

    if sqrt - math.floor(sqrt) < 0.5:
        return math.floor(sqrt)
    else:
        return math.ceil(sqrt)


print(rounded_sqrt(int(input())))


# Напишите функцию sin_of_angle(angle: float) -> float,
# которая принимает угол в градусах и возвращает значение синуса этого угла, используя math.radians() и math.sin().

import math


def sin_of_angle(angle: float) -> float:
    angle_in_radians = math.radians(angle)

    sin_value = math.sin(angle_in_radians)

    return round(sin_value, 1)


print(sin_of_angle(int(input())))


# Напишите функцию hypotenuse(a: float, b: float) -> float,
# которая возвращает длину гипотенузы прямоугольного треугольника с катетами a и b, используя math.hypot().

import math


def hypotenuse(a, b):
    return math.hypot(a, b)


a, b = list(map(int, input().split(", ")))

print(hypotenuse(a, b))
