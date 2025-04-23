# Напишите многопоточную программу, использующую ThreadPoolExecutor для конкурентного вычисления среднего балла оценок студентов. Программа должна принимать словарь, содержащий идентификаторы студентов и информацию о них (включая оценки). Каждый поток должен обрабатывать данные отдельного студента, вычисляя средний балл его оценок и округляя результат до двух десятичных знаков. Итоговый результат — вывод словаря, где ключами являются имена студентов, а значениями — их средние баллы.
# Описание:
#
# Начните с создания экземпляра ThreadPoolExecutor. Укажите количество потоков (например, 5), которое определяет, сколько задач может выполняться одновременно.
# Дан словарь, где ключи - это идентификаторы студентов, а значения - словари с информацией о студентах (имя, возраст, список оценок).
# # Полная версия этого словаря вшита в задачу
# students = {
#     1: {'name': 'Alice', 'age': 20, 'grades': [4, 5, 5, 4, 2, 3, 5, 2]},
#     2: {'name': 'Bob', 'age': 21, 'grades': [3, 4, 3, 4, 4, 5, 3, 4, 3, 2, 4]},
#     3: {'name': 'Charlie', 'age': 19, 'grades': [5, 5, 5, 5, 5, 5, 4, 5, 4, 5, 4]},
#     ...
#     20: {'name': 'Hannah Thompson', 'age': 20, 'grades': [2, 4, 3, 5, 3, 3, 2, 4, 4, 3, 2, 2, 2, 2, 5, 3, 4, 5]}
#     }
# Задача каждого потока - рассчитать средний балл каждого студента, округлить значение до двух символов после запятой.
# Используйте map() для распределения задач по студентам.
# Код должен сформировать и вывести словарь, где ключами будут имена студентов, а значениями — их средние баллы, как показано ниже.
# {'Alice': 3.75, 'Bob': 3.55, ..., 'Hannah Thompson': 3.22}

from concurrent.futures import ThreadPoolExecutor
from statistics import mean

students = {
    1: {"name": "Alice", "age": 20, "grades": [4, 5, 5, 4, 2, 3, 5, 2]},
    2: {"name": "Bob", "age": 21, "grades": [3, 4, 3, 4, 4, 5, 3, 4, 3, 2, 4]},
    3: {"name": "Charlie", "age": 19, "grades": [5, 5, 5, 5, 5, 5, 4, 5, 4, 5, 4]},
    20: {
        "name": "Hannah Thompson",
        "age": 20,
        "grades": [2, 4, 3, 5, 3, 3, 2, 4, 4, 3, 2, 2, 2, 2, 5, 3, 4, 5],
    },
}


class StudentGrades:
    def __init__(self, students: dict):
        self.students = students

    @staticmethod
    def calculate_average_grade(student_data: dict):
        name = student_data.get("name", "Unknown")
        grades_list = student_data.get("grades", [])

        avg_grade = round(mean(grades_list), 2)

        return (name, avg_grade)

    def calculate_all_grades(self):
        with ThreadPoolExecutor(max_workers=5) as executor:
            results = executor.map(self.calculate_average_grade, self.students.values())

            return dict(results)


def main():
    stud = StudentGrades(students)
    all_grades = stud.calculate_all_grades()

    print(all_grades)


main()
