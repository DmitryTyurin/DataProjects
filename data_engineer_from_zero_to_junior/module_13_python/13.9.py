# Напишите функцию count_vowels_consonants(s: str) -> dict, которая принимает строку и возвращает словарь с количеством гласных и согласных.

def count_vowels_consonants(s: str) -> dict:
    s = s.lower()
    count = {'vowels': 0, 'consonants': 0}

    for char in s:
        if char.isalpha():
            if char in 'aeiou':
                count['vowels'] += 1
            else:
                count['consonants'] += 1

    return count

print(count_vowels_consonants(input()))