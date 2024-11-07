# В данном задании, вам необходимо перевернуть строко-ориентированную таблицу, в столбцово-ориентированную таблицу (транспонировать),
# после чего посчитать сумму по первому столбцу.
# На данном примере вы сможете увидеть при столбцово ориантированной матрице проще применять различные функции агрегации.

matrix_list = list(map(str, input().split()))
size = 3
matrix = [matrix_list[i : i + size] for i in range(0, len(matrix_list), size)]


# Транспонируем матрицу
transposed_matrix = [[row[i] for row in matrix] for i in range(size)]

# Вычисляем сумму элементов первого столбца новой матрицы
first_column_sum = sum([int(item) for item in transposed_matrix[0]])

print(first_column_sum)


# Предлагаю вам решить задачу на сжатие данных. Вам передается строка вида AAaa вам необходимо написать алгоритм сжатия данных и получить A2a2

text = "AaaAAAAA"


def compress_text(input_text):
    compressed_text = ""
    i = 0
    while i < len(input_text):
        count = 1
        while i + 1 < len(input_text) and input_text[i] == input_text[i + 1]:
            i += 1
            count += 1
        if count > 1:
            compressed_text += input_text[i] + str(count)
        else:
            compressed_text += input_text[i]
        i += 1
    return compressed_text


print(compress_text(text))
