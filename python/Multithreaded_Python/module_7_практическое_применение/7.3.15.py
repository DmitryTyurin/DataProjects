# Вам предоставлен список учеников с их оценками по различным предметам students_grades. Некоторые ученики могли пропустить все экзамены, в результате чего у них нет оценок. Ваша задача - вычислить и вывести средний балл каждого ученика. Однако, если у ученика нет оценок, программа должна генерировать исключение, которое вы обработаете, выводя соответствующее сообщение.
#
# # Словарь с оценками студентов
# # Полный словарь вшит в задачу
#
# students_grades = {
#     "Иван": [5, 4, 3, 5],
#     "Алексей": [],
#     "Мария": [5, 5, 5, 5],
#     "Андрей": [4, 4, 3, 5],
# ...
# ...
# ...
# }
# Шаги выполнения задачи:
#
# Проанализируйте предоставленный словарь students_grades, где ключи - это имена учеников, а значения - списки их оценок.
#
# Словарь students_grades полностью, тащить в задачу не нужно!
# Для каждого ученика вычислите средний балл, используя оценки из списка. Если список оценок пуст, сгенерируйте исключение ValueError с сообщением о том, что у студента нет оценок.
#
# Средний балл Иван: 4.25
#
# print(f"Средний балл {student}: {average:.2f}")
# Для учеников без оценок обработайте исключение, выводя информацию о том, что у данного ученика нет оценок.
#
# У студента Дмитрий нет оценок.
#
# raise ValueError(f"У студента {student} нет оценок.")
# Используйте изученные методы, чтобы параллельно обработать данные всех учеников.
#
# Вывод программы должен быть следующий:

from concurrent.futures import ThreadPoolExecutor
from threading import Lock
import time

students_grades = {
    "Иван": [5, 4, 3, 5],
    "Алексей": [],
    "Мария": [5, 5, 5, 5],
    "Андрей": [4, 4, 3, 5],
    "Екатерина": [3, 4, 5, 4],
    "Петр": [5, 5, 4, 4],
    "Наталья": [3, 4, 4, 3],
    "Сергей": [4, 4, 4, 5],
    "Анна": [5, 4, 5, 5],
    "Дмитрий": [],
    "Елена": [3, 4, 4, 3],
    "Алина": [5, 5, 5, 5],
    "Артем": [4, 4, 5, 4],
    "Ольга": [5, 4, 3, 5],
    "Ирина": [4, 3, 5, 5],
    "Константин": [],
    "Татьяна": [3, 4, 5, 5],
    "Владимир": [4, 4, 5, 4],
    "Юлия": [5, 5, 5, 5],
    "Валентин": [],
    "Светлана": [3, 4, 3, 3],
    "Виктор": [5, 4, 5, 5],
    "Галина": [4, 4, 4, 4],
    "Роман": [5, 4, 5, 4],
    "Михаил": [4, 4, 5, 4],
    "Оксана": [],
    "Лариса": [4, 4, 3, 5],
    "Даниил": [5, 5, 5, 5],
    "Максим": [4, 4, 5, 4],
    "Валерия": [3, 3, 4, 4],
}


class StudentAverageGrades:
    def __init__(self, students_grades: dict):
        self.students_grades = students_grades
        self.executor: ThreadPoolExecutor = ThreadPoolExecutor(max_workers=3)
        self.lock: Lock = Lock()

    def calculate_average_grades(self, student_name: str, grades: list):
        with self.lock:
            try:
                if not grades:
                    raise ValueError(f"У студента {student_name} нет оценок.")

                average_grade = sum(grades) / len(grades)
                return f"Средний балл {student_name}: {average_grade:.2f}"
            except Exception as e:
                return e

    def run(self):
        with self.executor as executor:
            futures = [
                executor.submit(self.calculate_average_grades, student_name, grades)
                for student_name, grades in self.students_grades.items()
            ]

            for future in futures:
                result = future.result()
                print(result)


average_grades = StudentAverageGrades(students_grades)
average_grades.run()
