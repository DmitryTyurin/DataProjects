# Напишите функцию calculate_high_low_avg, которая принимает произвольное количество позиционных аргументов в виде целых чисел. Функция находит среднее арифметическое самого большого и самого маленького из аргументов и возвращает в качестве ответа.
#
# К тому же если в calculate_high_low_avg передать необязательный именованный аргумент log_to_console со значением True, то дополнительно функция должна вывести на экран информацию в следующем формате:
#
# high={max}, low={min}, avg={average}
# где max - принимает значение самого большого аргумента, min - принимает значение самого маленького аргумента, average - принимает среднее арифметическое самого большого и самого маленького из аргументов.
# Напомню что return сразу же производит выход из функции.
def calculate_high_low_avg(*args, log_to_console=False):
    if args:
        max_value = max(args)
        min_value = min(args)
        average = (max_value + min_value) / 2
        if log_to_console:
            print(f'high={max_value}, low={min_value}, avg={average}')
        return average
    else:
        return None




