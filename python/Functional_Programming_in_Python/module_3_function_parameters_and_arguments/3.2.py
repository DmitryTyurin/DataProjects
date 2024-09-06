# Напишите функцию words_length, которая по входному списку слов создает список целых чисел,
# составленный из длины соответствующих слов и возвращает его в качестве результата.


def words_length(words):
    return [len(word) for word in words]


# Напишите функцию filter_long_words, которая принимает список слов и целое число N
# и возвращает список слов, длина которых больше чем число N


def filter_long_words(words, N):
    return [word for word in words if len(word) > N]


# Напишите функцию is_member, которая принимает некое значение value и список значений lst.
# Функция is_member должна вернуть True, если значение value присутствует в списке lst, и False в противном случае.
# Гарантируется, что список lst не будет вложенным


def is_member(value, lst):
    return value in lst


# Определите функцию overlapping, которая принимает два списка и возвращает True,
# если у них есть хотя бы один общий элемент, в противном случае — False.
# ВЫ можете решать задачу удобным для вас способом,
# но попробуйте реализовать с использованием функции is_member из предыдущего шага.


def is_member(value, lst):
    return value in lst


def overlapping(lst1, lst2):
    for value in lst1:
        if is_member(value, lst2):
            return True
    return False


# Напишите функцию find_longest_word_len, которая принимает список слов и возвращает длину самого длинного из них.


def find_longest_word_len(words):
    return max(len(word) for word in words)


# Напишите функцию register_check, которая проверяет сколько человек успешно прошло регистрацию на мероприятие.
# Функция принимает словарь в качестве параметра, состоящий из имен людей(ключи) и результатов регистрации(значения ключа).
# Если человек успешно прошел регистрацию, то в словаре напротив его имени хранится значение «yes», иначе «no».
# Функция register_check должна возвращать количество только тех людей, кто успешно зарегистрировался.


def register_check(registration_dict):
    return sum(1 for result in registration_dict.values() if result == "yes")


# Напишите функцию create_tuples, которая принимает два списка одинаковой длины и объединяет их в список кортежей.
# Элемент кортежа получается путем соединения элемента первого и второго списков, стоящих на одинаковых позициях
def create_tuples(lst1, lst2):
    return [(x, y) for x, y in zip(lst1, lst2)]
