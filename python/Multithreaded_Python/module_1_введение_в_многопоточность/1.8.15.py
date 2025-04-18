# Ваша задача, заключается в том, чтобы организовать секретную операцию с использованием кодовых имен. У вас есть список из 15 уникальных кодовых имен для агентов.
#
# # Полный список вшит в задачу
# code_names = [
#     "Alpha", "Bravo", ...,
# ]
# Ваша задача — запустить потоки, где каждому потоку будет присвоено одно из этих кодовых имен из списка. Важно не только запустить потоки, но и сопроводить их соответствующими уведомлениями о статусе их миссий.
#
# Напишите функцию task(), которая будет выполняться в каждом потоке. Эта функция должна имитировать задержку при выполнении задачи и завершаться сообщением о том, что задача выполнена.
# Пример сообщения:
#
# Задача выполнена для Delta
#
# print(f"Задача выполнена для {threading.current_thread().name}")
# Запустите 15 потоков, следуя изложенной ниже последовательности. Важно отслеживать каждый шаг операции:
#
# Сначала напечатайте имя потока, полученное им при создании:
# Исходное имя потока: Thread-1 (task)
#
# print(f"Исходное имя потока: {thread.name}")
# Обратите внимание на то, что потоки, создаваемые threading.Thread(target=task), имеют имя вида
# Thread-1 (task) - в скобках имя целевой функции.
#
# Измените имя потока на соответствующее кодовое имя из вашего списка и снова напечатайте, но уже новое имя потока.
# Новое имя потока: Alpha
#
# print(f"Новое имя потока: {thread.name}")

from threading import Thread, current_thread
import time

# Список кодовых имен агентов
code_names = [
    "Alpha",
    "Bravo",
    "Charlie",
    "Delta",
    "Echo",
    "Foxtrot",
    "Golf",
    "Hotel",
    "India",
    "Juliet",
    "Kilo",
    "Lima",
    "Mike",
    "November",
    "Oscar",
]


def task():
    current_thread_name = current_thread().name

    time.sleep(1)
    print(f"Задача выполнена для {current_thread_name}")


def main():
    threads = []

    for i, code_name in enumerate(code_names):
        thread = Thread(target=task, name=f"Thread-{i + 1} (task)")
        threads.append(thread)

        print(f"Исходное имя потока: {thread.name}")

        thread.name = code_name
        print(f"Новое имя потока: {thread.name}")

        thread.start()

    [tread.join() for tread in threads]


main()
