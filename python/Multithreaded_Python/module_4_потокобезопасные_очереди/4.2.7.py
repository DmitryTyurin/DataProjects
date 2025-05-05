# У вас есть список текстовых файлов. Для каждого файла необходимо создать 2 потока. Первый поток должен определить общее количество слов в каждом файле, а второй поток должен определять общее количество строк в каждом файле. Результаты вычислений каждого потока необходимо сохранить в отдельные очереди.
#
# Используйте следующие файлы : file1.txt, file2.txt, file3.txt
#
# Просуммируйте полученные значения для всех трех файлов, поместите результаты  в соответствующие переменные ниже и нажмите отправить.

import threading
import queue
import os
import time

files = ["file1.txt", "file2.txt", "file3.txt"]


class DataMultiplexer:
    def __init__(self, files):
        self.files = files
        self.word_queue = queue.Queue()
        self.line_queue = queue.Queue()
        self.threads = []

    def count_words(self):
        try:
            with open(self.files, "r") as f:
                words = f.read().split()
                self.word_queue.put(len(words))
        except FileNotFoundError:
            self.word_queue.put(0)

    def count_lines(self):
        try:
            with open(self.files, "r") as f:
                lines = f.readlines()
                self.line_queue.put(len(lines))
        except FileNotFoundError:
            self.line_queue.put(0)

    def run_threads(self):
        for file in files:
            count_words_threads = threading.Thread(
                target=self.count_words, args=(file,)
            )
            count_lines_threads = threading.Thread(
                target=self.count_lines, args=(file,)
            )

            count_words_threads.start()
            count_lines_threads.start()

            self.threads.extend([count_words_threads, count_lines_threads])

        [t.join() for t in self.threads]

    def summary_results(self):
        total_words = sum(self.word_queue.queue)
        total_lines = sum(self.line_queue.queue)

        print(
            f"общее количество слов: {total_words}\n"
            f"общее количество строк: {total_lines}\n"
        )


data = DataMultiplexer(files)
data.summary_results()
