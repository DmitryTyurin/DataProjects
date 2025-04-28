# Немного изменим условие выполнения предыдущей задачи!
# Напишите программу, которая будет вычислять квадрат передаваемого числа или его факториал, в зависимости от его величины.
#
# Используйте следующую последовательность чисел:
#
# ​​​​​​​numbers = [3, 6, 14, 20, 5, 7, 2]
# Ключевые моменты:
#
# Определите функцию для обработки числа. Если число меньше или равно семи, то необходимо вычислить его факториал, если больше - его квадрат. Функция должна сообщать о начале обработки числа, в виде:
# Обработка числа <число> началась
# затем она должна имитировать время работы, в виде задержки в 1/10 секунды от передаваемого числа,
# ​​​​​​​производить необходимые вычисления и возвращать переданное число и полученный результат вычислений;
# В главном потоке создайте, без использования контекстного менеджера, пул с числом потоков равным количеству передаваемых чисел;
# Создайте задачи и передайте их в пул.
# Сразу после этого "закройте" созданный пул потоков без ожидания завершения всех задач.
# С целью проверки закрытия пула потоков выдержите паузу в 0.1 секунды и попытайтесь передать в него еще одну задачу:
# time.sleep(.1)
# executor.submit(answer, 42)
# В случае возникновения исключения перехватите его и выведите сообщение:
#
# Пул потоков остановлен! Передача новых задач в него невозможна!
# Организуйте вывод на печать результатов по мере выполнения задач в виде:
# Результат обработки <число> = <результат>


from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import math

numbers = [3, 6, 14, 20, 5, 7, 2]


class FactorialSquare:
    def __init__(self, numbers: list):
        self.number = numbers
        self.executor = ThreadPoolExecutor(len(self.number))
        self.result = []

    @staticmethod
    def worker(number: int):
        print(f"Обработка числа {number} началась")
        time.sleep(0.1)

        if number <= 7:
            result = math.factorial(number)
        else:
            result = number**2

        return number, result

    def run(self):
        with self.executor as executor:
            futures = [executor.submit(self.worker, number) for number in self.number]
            executor.shutdown(wait=False)

        time.sleep(0.1)
        try:
            executor.submit(self.worker, 42)
        except RuntimeError:
            print("Пул потоков остановлен! Передача новых задач в него невозможна!")

        for future in as_completed(futures):
            number, result = future.result()
            self.result.append((number, result))

        self.result = sorted(self.result)

        for number, result in self.result:
            print(f"Результат обработки {number} = {result}")


FactorialSquare(numbers).run()
