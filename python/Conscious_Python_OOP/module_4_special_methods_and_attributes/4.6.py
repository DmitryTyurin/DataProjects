# Создайте подходящие методы, чтобы результат стал верным.
# Внимательно присмотритесь к уже написанному коду и результату, и проявите изобретательность.


class MyPhone:
    def __init__(self):
        self.phone = ["Nokia", "Iphone", "Samsung", "Huawei", "LG"]

    def __str__(self):
        return str(self.phone)

    def __getitem__(self, item):
        return self.phone[item]

    def __setitem__(self, index, value):
        self.phone[index] = value

    def __delitem__(self, index):
        del self.phone[index]

    def kruchu_verchu(self, brand):
        self.phone.append(brand)


my_phone = MyPhone()

my_phone[1] = "Xiaomi"
del my_phone[2]
my_phone.kruchu_verchu("HONOR")

print(my_phone)
print(my_phone[4])


# Машенька очень хочет снеговика (snowman) на Новый Год. Помогите ей получить этот подарок! Допишите код так, чтобы в конце, на экране появилось слово snowman. Проявите изобретательность и внимательно посмотрите на уже написанный код.


class Present:
    def __init__(self):
        self.present = ["book", "Iphone", "TV", "snowman", "car"]

    def __len__(self):
        return len(self.present)

    def __getitem__(self, index):
        return self.present[index]


holiday = Present()
holiday.present.remove("car")

if len(holiday) == 4:
    print(holiday[3])


# Машенька мечтает слетать в Казахстан к своему другу Васе, помогите ей осуществить мечту. Часть кода уже написана. Вам нужно лишь создать подходящий метод или методы.


class Country:
    country = ("Russia", "Ukraine", "Belarus", "Kazakhstan", "Other")

    def __iter__(self):
        return iter(self.country)


country_is = Country()
for i in country_is:
    if i == "Kazakhstan":
        print(f"Ура, Маша летит в Казахстан!")


# Часть кода уже написана. Вам нужно лишь объявить два метода: __iter__ , __next__
# Метод __iter__ выполняет две задачи:
# - Выводит на экран текст: "Запустился __iter__".
# - Возвращает self, чтобы код правильно работал.
# Метод __next__ выполняет две задачи (обе задачи выполняются внутри метода):
# - Выводит на экран текст: "Запустился __next__".
# - Имеет стандартный код с условием (if, else), чтобы экземпляры можно было использовать в циклах. Подсказка, смотрите первый пример в статье про __iter__ , __next__. Итерации будут происходить по атрибуту data, поэтому создайте соответствующие проверки и исключение raise StopIteration. Метод ничего не возвращает, т.е. без return.
# В результате всего кода, мы получим на экране 5 сообщений (см. ответы ниже). Объявите только методы, всё остальное появится в результате цикла.


class MyList:
    def __init__(self):
        self.data = [1, 2, 3]
        self.index = 0

    def __iter__(self):
        self.index = 0

        print("Запустился __iter__")

        return self

    def __next__(self):
        print("Запустился __next__")

        if self.index < len(self.data):
            self.index += 1

            return self.data[self.index - 1]
        else:
            raise StopIteration


# код ниже пожалуйста не меняйте
my_list = MyList()
for i in my_list:
    pass
