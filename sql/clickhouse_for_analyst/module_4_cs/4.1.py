# Вам необходимо посчитать сумму, нельзя использовать функцию sum.
# Для решения вам нужно пройтись по массиву чисел и посчитать сумму например с помощью for.
# Это важно для следующего шага.

array = list(map(int, input().split()))

result = 0
for number in array:
    result += number

print(result)


# Предлагаю вам такую задачу, воспользуйтесь предыдущим алгоритмом и дополните его так чтобы функция возвращала элемент
# ближайший по значению к заданному (в большую сторону).
# В данной задаче нет пограничных случаев, можно их не разбирать, и в случае нахождения target в списке,
# все равно нужно вывести большее значение.
# Ваша задача только реализовать функцию


def binary_search(arr: list, target: int) -> int | float | None:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            if mid < len(arr) - 1:
                return arr[mid + 1]
            else:
                return None

        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    if left < len(arr):
        return arr[left]
    else:
        return None


arr, target = list(map(str, input().split(",")))

arr = list(map(int, arr.split()))  # Массив
target = int(target)  # Таргет

print(binary_search(arr, target))

# Давайте потренируемся в использовании хеш таблиц и вспомним про сложность алгоритмов.
# Напишите функцию find_duplicates, которая принимает список целых чисел и возвращает список всех повторяющихся элементов в исходном списке, то есть тех элементов которых больше 1
# Чтобы решить данную задачу используйте dict который является хеш таблицей в Python.
# Нельзя использовать дополнительные библиотеки и структуры, только стандартный Python!

# Считывание данных
array = list(map(str, input().split()))


def find_duplicates(numbers):
    count = {}
    duplicates = []
    for num in numbers:
        if num in count:
            count[num] += 1
            if count[num] == 2 and num not in duplicates:
                duplicates.append(num)
        else:
            count[num] = 1
    return duplicates


duplicates = find_duplicates(array)
print(" ".join(sorted(duplicates)))


# Реализуйте алгоритм LEFT HASH JOIN. Это значит что левая таблица будет выведена полностью,
# а правая только если есть совпадение.
# В итоге вы должны получить словарь в котором ключами будут данные из левой таблицы,
# а значениями данные из правой таблицы, если совпадения не было найдено, то в значении должно лежать 'default'.
# В переменной left лежит список, в right лежит словарь, где ключи совпадают с данными списка.
# Вывод на печать в формате ключ: значение, пример дан ниже.
# Подсказка - необязательно прям формировать словарь, можно сразу выводить на печать.

left, right = list(map(str, input().split(",")))

left = list(map(str, left.split()))
right = dict(map(lambda x: x.split(":"), right.split()))

for item in left:
    if item in right:
        print(f"{item}:{right[item]}")
    else:
        print(f"{item}:default")

