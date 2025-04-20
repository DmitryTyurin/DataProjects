# Напишите программу, которая имитирует работу космической станции.
#
# Ключевые моменты:
#
# Определите функцию для имитации работы космонавта, которая будет выводить:
# <имя космонавта> выполняет задачу: <название задачи>
# Определите функцию для имитации работы космической станции. Передайте в функцию аргументы: intervals, astronauts, tasks
# Используйте заданные имена и порядок их передачи. Списки вшиты в тестирующую систему!
# intervals - список интервалов для выполнения задач
# astronauts - список астронавтов
# tasks - список задач для выполнения астронавтов
# Данные для тестирования
# astronauts = ["Алексей Леонов", "Юрий Гагарин", "Джон Гленн"]
# tasks = ["Ремонт оборудования", "Проведение экспериментов", "Мониторинг систем"]
# intervals = [0.7, 1.3, 1.8]
#
#
# Функция назначает задачу каждому астронавту, и он отправляется ее выполнять через заданный интервал времени.

import threading


# Данные для тестирования
astronauts = ["Алексей Леонов", "Юрий Гагарин", "Джон Гленн"]
tasks = ["Ремонт оборудования", "Проведение экспериментов", "Мониторинг систем"]
intervals = [0.7, 1.3, 1.8]


class AstronautProcess:
    def __init__(self, astronaut, task, interval):
        self.astronaut = astronaut
        self.task = task
        self.interval = interval

    def run(self) -> None:
        threading.Timer(self.interval, self.astronaut_task).start()

    def astronaut_task(self) -> None:
        print(f"{self.astronaut} выполняет задачу: {self.task}")


def space_station(intervals: list, astronauts: list, tasks: list) -> None:
    for astronaut, task, interval in zip(astronauts, tasks, intervals):
        astronaut_process = AstronautProcess(astronaut, task, interval)
        astronaut_process.run()


space_station(intervals, astronauts, tasks)
