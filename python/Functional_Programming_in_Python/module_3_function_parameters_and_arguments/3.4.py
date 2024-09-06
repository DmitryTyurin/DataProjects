# Напишите функцию product , которая принимает список чисел и находит их произведение. Также данная функция может принимать необязательный параметр start , который отвечает за начальное значение произведения (по умолчанию равно 1)
def product(numbers, start=1):
    result = start
    for number in numbers:
        result *= number
    return result


# Ваша задача написать функцию add_item, которая добавляет в корзину (глобальная переменная shopping_list) товар и его количество.
#
# Функция add_item обязательно должна принимать имя товара и необязательно - его количество (по умолчанию оно равно 1)

shopping_list = {}


def add_item(name, count=1):
    if name in shopping_list:
        shopping_list[name] += count
    else:
        shopping_list[name] = count


# Напишите функцию show_list, которая выводит список товаров из корзины(глобальная переменная shopping_list). У функции show_list есть необязательный логический параметр include_quantities, по умолчанию принимает значение True.
#
# Если include_quantities имеет значение правда, вы должны выводить имя товара и его количество в формате
#
# {количество}x{имя_товара},
#
# иначе выводите только имя.
#
# Напишите только реализацию функции show_list


def show_list(include_quantities=True):
    for item in shopping_list:
        if include_quantities:
            print(f"{shopping_list[item]}x{item}")
        else:
            print(item)


# Исправьте функции так, чтобы добавление одной оценки студенту не влияло на оценки других учеников


def create_student(name, age, marks=[]):
    return {"name": name, "age": age, "marks": marks}  # оценки


def add_mark(student, mark):
    new_marks = student["marks"][:]  # создаем копию списка оценок
    new_marks.append(mark)  # добавляем новую оценку
    student["marks"] = new_marks  # заменяем старый список оценок на новую копию


# Мы часто сталкиваемся с математической проблемой, когда после совместного похода в ресторан необходимо посчитать сколько должен каждый человек. Давайте создадим функцию  calculate_per_person, которая поможет выполнить расчет.
#
# Будем считать, что у нас идеальная ситуация, когда между N количеством людей нужно разделить счет поровну. Также в счет нужно включить чаевые официанту, которые по умолчанию составляют 10%.
#
# Итого получаем, что функция calculate_per_person может принимать следующие аргументы
#
# обязательно счет за ресторан
# обязательно количество людей
# необязательно процент чаевых официанту, по умолчанию 10%
# Функция calculate_per_person должна вернуть результат - сумму, которую должен заплатить каждый участник ужина.
#
# При расчете у  вас будут возникать вещественные числа, результат нужно будет округлять функцией round до второго разряда после запятой


def calculate_per_person(total_bill, people_count, tip_percent=10):
    tip_amount = total_bill * tip_percent / 100
    total_bill_with_tip = total_bill + tip_amount
    return round(total_bill_with_tip / people_count, 2)


# Помните у нас была реализована функция reserve_table ? Она принимала три обязательных значения: номер стола, имя клиента и статус VIP.
#
# Как только менеджеры узнали про параметр со значением по умолчанию они сразу решили попросить вас переписать функцию reserve_table так, чтобы статус VIP клиента был по умолчанию равен False. Потому что большинство клиентов не так часто заходят в данное заведение и по статистике больше обычных клиентов, нежели вип-персон.

tables = {
    1: {"name": "Andrey", "is_vip": True},
    2: None,
    3: None,
    4: None,
    5: {"name": "Vasiliy", "is_vip": False},
    6: None,
    7: None,
    8: None,
    9: None,
}


def is_table_free(table_number):
    return tables[table_number] is None


def reserve_table(table_number, client_name, is_vip=False):
    if is_table_free(table_number):
        tables[table_number] = {"name": client_name, "is_vip": is_vip}


def delete_reservation(table_number):
    tables[table_number] = None
