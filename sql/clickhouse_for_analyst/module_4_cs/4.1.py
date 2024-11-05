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
