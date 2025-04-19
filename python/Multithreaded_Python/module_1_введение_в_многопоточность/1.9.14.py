# Вам предстоит модифицировать данный код, чтобы он корректно использовал локальное хранилище данных в многопоточном контексте. Исходный код создаёт несколько потоков, в которых должны устанавливаться и выводиться данные из локального хранилища каждого потока.
#
# Задача заключается в следующем:
#
# Необходимо обеспечить, чтобы каждый поток независимо сохранял и обрабатывал значение 'HELLO LOCAL STORAGE!' в своём локальном хранилище.
# Функция process_data() уже готова выводить данные из хранилища, вам осталось только создать его и указать его содержимое.
#
#
# Вывод кода после изменения должен быть такой.
#
# Данные в локальном хранилище: HELLO LOCAL STORAGE!
# Данные в локальном хранилище: HELLO LOCAL STORAGE!
# Данные в локальном хранилище: HELLO LOCAL STORAGE!

import threading

STORAGE_DATA = "HELLO LOCAL STORAGE!"


class LocalStorage:
    def __init__(self, storage_data: str):
        self.storage_data = storage_data
        self.treads = []
        self.thread_data = threading.local()

    def process_data(self):
        print(f"Данные в локальном хранилище: {self.thread_data.data}")

    def worker(self):
        self.thread_data.data = self.storage_data
        self.process_data()

    def run_threads(self):
        for x in range(3):
            t = threading.Thread(target=self.worker)
            self.treads.append(t)
            t.start()

        [t.join() for t in self.treads]


ls = LocalStorage(STORAGE_DATA)
ls.run_threads()
