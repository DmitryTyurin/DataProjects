# Описание задачи:
#
# Представьте, что вы работаете в крупной компании, где совещания - часть повседневной жизни. Ваша задача как разработчика программного обеспечения для управления офисом - создать систему оповещения сотрудников о начале совещания. Система должна учитывать, что все сотрудники могут находиться в разных частях здания и иметь разное время реакции на уведомление. Используя многопоточность и барьерную синхронизацию, вы должны организовать процесс так, чтобы все сотрудники прибыли на совещание одновременно.
#
# Шаги выполнения задачи:
#
# Используйте предоставленный словарь employee_times, где ключи - это имена сотрудников, а значения - время, необходимое им для прибытия на совещание после получения уведомления.
#
# # Полный список вшит в задачу (значения в списке генерируются случайным образом)
#
# employee_times = {
#     'Алиса': 4.44,
#     'Боб': 7.33,
#     'Чарли': 7.75,
#     ...
#     ...
#     ...,
#     }
# Инициализируйте барьер таким образом, чтобы его порог соответствовал общему количеству сотрудников. Это обеспечит, что поток каждого сотрудника будет ожидать у барьера до тех пор, пока не прибудут все остальные.
#
# Для каждого сотрудника создайте поток, который симулирует их действия:
#
# Начало движения к месту совещания.
#
# Алиса начал(а) идти на совещание.
#
# print(f'{name} начал(а) идти на совещание.')
# И прибытие на место.
#
# Роза прибыл(а) на совещание, затратив 1.34 секунд.
#
# print(f'{name} прибыл(а) на совещание, затратив {time_to_arrive} секунд.')
# Используйте time.sleep() для имитации времени на путь.
#
# После того как все сотрудники прибудут (то есть все потоки достигнут барьера), совещание может начаться. Отметьте это момент сообщением:
#
# Совещание началось!
#
# print("Совещание началось!")
# Технические детали:
#
# Примените метод barrier.wait() для ожидания прибытия всех участников совещания.
# Выведите сообщения о начале движения к месту совещания и о прибытии для каждого сотрудника.

from concurrent.futures import ThreadPoolExecutor
from threading import Barrier, Lock
import time
import random

employee_times = {
    "Алиса": round(random.uniform(1, 10), 2),
    "Боб": round(random.uniform(1, 10), 2),
    "Чарли": round(random.uniform(1, 10), 2),
    "Дэвид": round(random.uniform(1, 10), 2),
    "Ева": round(random.uniform(1, 10), 2),
    "Фрэнк": round(random.uniform(1, 10), 2),
    "Грейс": round(random.uniform(1, 10), 2),
    "Хэнк": round(random.uniform(1, 10), 2),
    "Айви": round(random.uniform(1, 10), 2),
    "Джек": round(random.uniform(1, 10), 2),
}


class Meeting:
    def __init__(self, employee_times: dict):
        self.employee_times = employee_times
        self.barrier: Barrier = Barrier(len(self.employee_times))
        self.executor = ThreadPoolExecutor(max_workers=len(self.employee_times))
        self.lock: Lock = Lock()

    def lprint(self, text: str) -> None:
        with self.lock:
            print(text)

    def getting_ready(self, name: str, time_to_arrive: float | int) -> None:
        self.lprint(f"{name} начал(а) идти на совещание.")

        time.sleep(time_to_arrive)

        self.barrier.wait()

        self.lprint(f"{name} прибыл(а) на совещание, затратив {time_to_arrive} секунд.")

    def start(self) -> None:
        with self.executor as executor:
            futures = executor.map(
                self.getting_ready,
                self.employee_times.keys(),
                self.employee_times.values(),
            )

        print("Совещание началось!")


meeting = Meeting(employee_times)
meeting.start()
