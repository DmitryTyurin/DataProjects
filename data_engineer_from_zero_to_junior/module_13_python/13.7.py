# Напишите программу, которая находит наиболее часто встречающийся элемент в списке. Если таких элементов несколько, выведите любой из них.

from collections import Counter

lst = list(map(int, input().split()))

counter = Counter(lst).most_common(1)

print("Наиболее часто встречающийся элемент:", counter[0][0])


# Напишите программу, которая принимает строку и подсчитывает, сколько раз каждое слово встречается в предложении.
# Выведите результат в виде словаря, где ключи — слова, а значения — их частота.

sentence = input()
words = sentence.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)


# Дано несколько кортежей, каждый из которых содержит по два элемента (a, b).
# Напишите программу, которая находит кортеж с наибольшей суммой элементов и кортеж с наименьшей суммой элементов.

tuples = eval("[" + input("").replace(" ", ",") + "]")

max_sum = max(tuples, key=lambda x: x[0] + x[1])
min_sum = min(tuples, key=lambda x: x[0] + x[1])

print("Кортеж с наибольшей суммой:", max_sum)
print("Кортеж с наименьшей суммой:", min_sum)


# Напишите программу, которая принимает список чисел и создает словарь, в котором ключи — это сами числа, а значения — их квадраты.
# Выведите только те пары, где квадрат числа чётный.

num = list(map(int, input().split()))
num_dict = {}
squares = {x: x**2 for x in num}

for key, value in squares.items():
    if value % 2 == 0:
        num_dict[key] = value

print(f"Словарь квадратов чётных чисел: {num_dict}")


# Напишите программу, которая принимает на вход две строки и выводит все общие буквы в алфавитном порядке.
# Если общих букв нет, программа должна вывести "Общих букв нет".

set1, set2 = set(input()), set(input())

common_chars = sorted(set1.intersection(set2))

if len(common_chars) == 0:
    print("Общих букв нет")
else:
    print(f"Общие буквы: {', '.join(common_chars)}")

