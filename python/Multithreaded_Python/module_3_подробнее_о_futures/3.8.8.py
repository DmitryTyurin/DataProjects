# Напишите программу, которая позволит отменить задачи, согласно заданному условию.
#
# Ключевые моменты:
#
# Напишите функцию, которая будет принимать элемент словаря, ключом которого будет число - время выполнения задачи, а значением строка - название задачи. После имитации заданной длительности выполнения функция должна выводить в консоль:
#           Задача <название задачи> выполнилась.
#
# После того как задачи будут отправлены в пул на выполнение, необходимо отменить те из них, у которых последняя цифра времени выполнения является нечетной.
# Для передачи аргументов функции используйте следующий словарь:
#
# data = {1.4: 'ljeo', 0.4: 'akwx', 2.3: 'tydx', 2.7: 'qnai', 2.6: 'smgx',
#         1.9: 'fhef', 1.6: 'wzag', 2.5: 'hjsz', 2.4: 'gpay', 0.5: 'wxco'}
# Будьте внимательны:
#
# Отменить можно только те задачи, которые еще не начали выполнение.
# Значение максимального количества потоков в пуле потоков будет влиять на итоговый результат (при запуске всех задач одновременно, отменить лишние задачи не получится).

from concurrent.futures import ThreadPoolExecutor


data = {
    1.4: "ljeo",
    0.4: "akwx",
    2.3: "tydx",
    2.7: "qnai",
    2.6: "smgx",
    1.9: "fhef",
    1.6: "wzag",
    2.5: "hjsz",
    2.4: "gpay",
    0.5: "wxco",
}


class TaskProcessor:
    def __init__(self, data: dict):
        self.data = data
        self.executor = ThreadPoolExecutor(max_workers=5)
        self.futures = []

    @staticmethod
    def process(duration: float, task_name: str):
        import time

        time.sleep(duration)

        return duration, task_name

    def run(self):
        with self.executor as executor:
            for duration, task_name in self.data.items():
                future = executor.submit(self.process, duration, task_name)
                self.futures.append(future)

            for future in self.futures:
                duration, task_name = future.result()
                last_digit = int(str(duration).replace(".", "")[-1])

                if last_digit % 2 != 0:
                    future.cancel()
                else:
                    print(f"Задача {task_name} выполнилась.")


tp = TaskProcessor(data)
tp.run()
