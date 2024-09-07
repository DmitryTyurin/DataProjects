# Создадим функцию print_scores, которая выводит результаты, набранные учеником в тесте.
#
# Функция принимает имя студента и его оценки, их может быть произвольное количество.
#
# Функция сперва выводит имя студента, а затем на отдельных строках все его оценки в порядке возрастания


def print_scores(name, *scores):
    print("Student name:", name)
    for score in sorted(scores):
        print(score)


# Напишите функцию truncate_sentences, которая обрезает предложения и оставляет из них только первые N символов.
# Количество предложений, которые поступают на вход функции, может быть произвольным


def truncate_sentences(n, *sentences):
    for sentence in sentences:
        print(sentence[:n])


# Напишите make_strings_big, которая должна принимать произвольное количество фраз и выводить каждую в отдельной строке, превращая все буквы в заглавные.
#
# Казалось бы простая функция, но у нее есть особенность - необязательный параметр reverse со значением по умолчанию False.
#
# Если передать в reverse True, функция make_strings_big должна делать обратное: преобразовывать все буквы в строчные.
def make_strings_big(*strings, reverse=False):
    for string in strings:
        if reverse:
            print(string.lower())
        else:
            print(string.upper())
