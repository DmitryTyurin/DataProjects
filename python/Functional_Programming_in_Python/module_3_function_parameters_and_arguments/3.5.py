# Помните функцию words_length, которая по входному списку слов создавала список длины соответствующих слов и возвращала его в качестве результата? Одна из возможных реализаций этой функции представлена ниже
#
# def words_length(words):
#     return [len(word) for word in words]
# Здесь функция words_length является чистой. Ваша задача переписать ее так, чтобы она начала изменять входной список: вместо слов должна подставляться его длина. В качестве результат новая words_length должна вернуть None


def words_length(words):
    for i in range(len(words)):
        words[i] = len(words[i])
    return None


# Перепишите функцию my_func так, чтобы она стала чистой
def my_func(collection, n):
    return collection + list(range(1, n + 1))
