# Скачайте архив с файлами. В каждом файле находятся три строки, каждая из которых содержит число от 0 до 999.
# Для каждого файла необходимо прочитать числа и проверить их. Если все числа в файле больше нуля, вам нужно их перемножить и добавить полученный результат к общему счетчику. Если же в файле встречается число 0, тогда сложите все числа в файле и вычтите эту сумму из общего счетчика.
# Используйте функцию map_async, чтобы обрабатывать файлы параллельно. Это позволит значительно ускорить процесс обработки файлов.
#
# По мере обработки файлов, результаты каждой операции нужно добавлять к глобальному счетчику, на первых итерациях, если первыми файлами являются те в которых есть 0, то допустимо чтобы глобальный счётчик опустился ниже нуля.
#
# После обработки всех файлов, выведите общую сумму, полученную в результате выполнения вышеописанных операций.
#
# # Замените *** на получившиеся значение
#
# print("Общая сумма чисел в файлах: ***")
# Ожидаемый результат:
# В консоли должно быть выведено сообщение вида: "Общая сумма чисел в файлах: X", где X — это общая сумма чисел, найденных во всех обработанных файлах. При этом, весь код на степик вставлять не нужно, необходимо вставить только print() с соответствующим числом.


from multiprocessing import freeze_support
from multiprocessing.pool import ThreadPool
import zipfile
import os


class DataReader:
    def __init__(self, folder_name: str):
        self.folder_name = folder_name
        self.current_dir = os.getcwd()
        self.folder_path = os.path.join(os.getcwd(), folder_name)
        self.pool = ThreadPool()

    def read_and_sum(self, file_path):
        with open(file_path, "r") as f:
            numbers = [int(line.strip()) for line in f if line.strip().isdigit()]
            if 0 in numbers:
                return -sum(numbers)
            else:
                product = 1
                for num in numbers:
                    product *= num
                return product

    def process_files(self):
        files = [
            os.path.join(self.folder_path, file_name)
            for file_name in os.listdir(self.folder_path)
            if file_name.endswith(".txt")
        ]
        with self.pool as pool:
            results = pool.map_async(self.read_and_sum, files)
            outputs = results.get()

        total = sum(outputs)
        print(f"Общая сумма чисел в файлах: {total}")


if __name__ == "__main__":
    freeze_support()

    reader = DataReader("output_files")
    reader.process_files()
