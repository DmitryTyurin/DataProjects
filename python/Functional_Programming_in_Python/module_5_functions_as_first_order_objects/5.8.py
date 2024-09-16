# Ваша задача создать функцию multiply, которая принимает один аргумент. Функция должна запомнить это значение, и вернуть результат умножения этого числа с переданным вновь значением (см. примеры)
#
# f_2 = multiply(2)
# print("Умножение 2 на 5 =", f_2(5)) #10
# print("Умножение 2 на 15 =", f_2(15)) #30
# f_3 = multiply(3)
# print("Умножение 3 на 5 =", f_3(5)) #15
# print("Умножение 3 на 15 =", f_3(15)) #45


def multiply(x):
    def inner(y):
        return x * y

    return inner


# Ваша задача создать функцию-замыкание make_repeater, которая должна дублировать переданную в нее строку N раз.
# При создании замыкания передается число N - количество для повторения.


def make_repeater(N):
    def repeater(s):
        return s * N

    return repeater


# Ваша задача создать функцию-замыкание create_accumulator, которая должна накапливать(суммировать) внутри себя все значения, которые ей будут переданы. При создании замыкания стартовая сумма должна быть равна нулю. Посмотрите пример ниже:
#
# summator_1 = create_accumulator()
# print(summator_1(1)) # печатает 1
# print(summator_1(5)) # печатает 6
# print(summator_1(2)) # печатает 8
#
# summator_2 = create_accumulator()
# print(summator_2(3)) # печатает 3
# print(summator_2(4)) # печатает 7
# При каждом вызове должна возвращаться накопленная сумма, которая хранится в замыкании.
#
# Обратите внимание, что объекты из примера summator_1 и summator_2 хранят и накапливают свои собственные суммы.
#
# Необходимо только определить функцию-замыкание create_accumulator, остальное мы сделаем за вас
def create_accumulator():
    def accumulator(x):
        nonlocal summ
        summ += x
        return summ

    summ = 0
    return accumulator


# На предыдущем шаге мы реализовали функцию-замыкание create_accumulator, которая накапливала сумму, начиная с нуля. Давайте ее усовершенствуем, чтобы она могла начинать суммировать, начиная с определенного значения. Это значение мы ей будем передавать, но оно является необязательным.  Посмотрите пример ниже:
#
# summator_1 = create_accumulator(100)
# print(summator_1(1)) # печатает 101
# print(summator_1(5)) # печатает 106
# print(summator_1(2)) # печатает 108
#
# summator_2 = create_accumulator()
# print(summator_2(3)) # печатает 3
# print(summator_2(4)) # печатает 7
# Во втором примере мы не передали значение и значит сумма по умолчанию должна считаться с нуля.
#
# Необходимо только определить функцию-замыкание create_accumulator, остальное мы сделаем за вас


def create_accumulator(start=0):
    def accumulator(x):
        nonlocal summ
        summ += x
        return summ

    summ = start
    return accumulator


# Напишите функцию-замыкание countdown, которая будет вести обратный отсчёт от переданного числа N до нуля. После того как замыкание будет вызвано более N раз необходимо выводить сообщение «Превышен лимит, вы вызвали более N раз»
def countdown(N):
    count = N

    def inner():
        nonlocal count
        if count > 0:
            print(count)
            count -= 1
        else:
            print(f"Превышен лимит, вы вызвали более {N} раз")

    return inner


# В этом задании вам нужно сделать функцию-замыкание count_calls, которая подсчитывает сколько раз она была вызвана.
# Особенность этого замыкания заключается в том, что количество вызовов должно храниться в атрибуте total_calls.
def count_calls():
    def inner():
        inner.total_calls += 1

    inner.total_calls = 0
    return inner


# Ваша задача создать функцию-замыкание create_dict. Функция create_dict должна сохранять в себе в виде словаря все значения, которые ей будут переданы. Ключами данного словаря должны быть натуральные числа, равные номеру вызова данной функции. Посмотрите пример ниже:
# f_1 = create_dict()
# print(f_1('hello')) # f_1 возвращает {1: 'hello'}
# print(f_1(100)) # f_1 возвращает {1: 'hello', 2: 100}
# print(f_1([1, 2, 3])) # f_1 возвращает {1: 'hello', 2: 100, 3: [1, 2, 3]}
# f_2 = create_dict() # создаем новое замыкание в f_2
# print(f_2('PoweR')) # f_2 возвращает {1: 'PoweR'}
# Вызывая первый раз f_1 мы создали пару 1: 'hello', вызывая второй раз добавилась пара 2: 100. и т.д.
# При каждом вызове должен возвращаться словарь, хранящийся в замыкании
# Необходимо только определить функцию-замыкание create_dict, остальное мы сделаем за вас


def create_dict():
    def inner(x):
        nonlocal dict_
        dict_[len(dict_) + 1] = x
        return dict_

    dict_ = {}
    return inner