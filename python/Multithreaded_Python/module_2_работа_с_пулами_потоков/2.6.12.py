# Ваша задача - написать программу, которая будет одновременно вычислять сумму или произведение чисел.
#
# Ключевые моменты:
#
# Напишите функцию, которая будет принимать 2 аргумента: время работы (имитация) и список чисел. Возвращаемое значение будет зависеть от времени работы - если время работы четное число, то функция возвращает произведение чисел, если же нечетное - сумму чисел;
# Используйте пул потоков для одновременного выполнения целевых функций для вычислений по каждому списку из numbers;
# Выведите результаты вычислений тех функций, работа которых не превышает 2.5 секунд.
#


from concurrent.futures import ThreadPoolExecutor, wait
import time

work_times = [4, 5, 3, 5, 4, 2, 5, 1, 3, 5, 3, 5, 1, 5, 5, 2, 1, 5, 1, 2]

numbers = [
    [2, 5],
    [6, 2],
    [9, 4],
    [2, 2],
    [2, 8],
    [3, 5],
    [4, 1],
    [6, 2],
    [7, 4],
    [9, 7],
    [5, 7],
    [3, 8],
    [4, 0],
    [8, 2],
    [6, 9],
    [9, 7],
    [3, 6],
    [6, 7],
    [2, 5],
    [7, 3],
]


class WorkWithNumbers:
    def __init__(self, work_times: list, numbers: list):
        self.work_times = work_times
        self.numbers = numbers

    @staticmethod
    def calculate(times: int, number_list: list) -> int:
        time.sleep(times)

        x = number_list[0]
        y = number_list[1]

        result = sum([x, y]) if times % 2 != 0 else x * y
        return result

    def run(self):
        with ThreadPoolExecutor(max_workers=len(self.numbers)) as executor:
            futures = {
                executor.submit(self.calculate, times, number_list)
                for times, number_list in zip(self.work_times, self.numbers)
            }

            done, not_done = wait(futures, timeout=2.5)

            [print(task.result()) for task in done]


def main() -> None:
    work = WorkWithNumbers(work_times, numbers)
    work.run()


main()
