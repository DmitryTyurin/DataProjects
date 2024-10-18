# Часть кода уже написана, используйте уже написанные данные и дополните код.
# Используйте в обязательной форме, методы __init__, __enter__ и __exit__.
# Планета Венера требовательная, и её можно указывать только в методе __exit__.
# Выведите все результаты согласно примеру ниже.

planetes = ["Сатурн", "Юпитер", "Земля", "Марс"]


class StarTravel:
    def __init__(self, other):
        self.planetes = planetes
        self.other = other

    def __enter__(self):
        return self.planetes

    def __exit__(self, exc_type, exc_value, traceback):
        print(self.other)
        print("Венера")
        pass


# код ниже пожалуйста не меняйте
with StarTravel("Плутон") as word:
    for i in word:
        print(i)
