# Ниже представлен код, который вам нужно будет дописать.
# В переменную from_10_to_20 при помощи генератора-выражения сохраните последовательность от 10 до 20 включительно
# Затем при помощи функции next выведите первые три элемента
# И остается вывести оставшиеся элементы в цикле
from_10_to_20 = (i for i in range(10, 21))
print(next(from_10_to_20))
print(next(from_10_to_20))
print(next(from_10_to_20))

for i in from_10_to_20:
    print(i)

# Перед вами список words
# Необходимо сохранить в переменной lens генератор-выражение, который генерирует длины слов списка words по порядку.
# Больше от вас в этой задаче ничего не требуется.

words = [
    "feel",
    "graduate",
    "movie",
    "fashionable",
    "bacon",
    "drop",
    "produce",
    "acquisition",
    "cheap",
    "strength",
    "master",
    "perception",
    "noise",
    "strange",
    "am",
]

lens = (len(word) for word in words)

for i in lens:
    print(i)
