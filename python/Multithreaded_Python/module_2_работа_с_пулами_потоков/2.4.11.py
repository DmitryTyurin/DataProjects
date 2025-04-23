# Цель задачи:
# Напишите многопоточную программу для подсчета количества символов в каждой строке из списка строк, используя ThreadPoolExecutor и его метод map().
#
# Список с данным:
#
# # Полный список messages вшит в задачу.
#
# messages = [
#     "Привет, давайте обсудим многопоточность в Python!",
#     "Да, GIL - это большая проблема для многопоточности в Python.",
# ]
# Использование функции map():
#
# Примените метод map() для распределения строк между потоками. Функция, передаваемая в map(), должна принимать одну строку из списка и возвращать количество символов в этой строке.
# Сбор и вывод результатов:
#
# Соберите результаты работы потоков, которые будут представлять собой количество символов в каждой строке. Выведите эти результаты в виде списка.
#
# Вывод программы должен быть следующим:
# Общее количество символов в каждой строке: [49, 60, ..., 85, 94]
#
# print(f"Общее количество символов в каждой строке: {character_counts}")

from concurrent.futures import ThreadPoolExecutor

messages = [
    "Привет, давайте обсудим многопоточность в Python!",
    "Да, GIL - это большая проблема для многопоточности в Python.",
]


class CharacterCounter:
    def __init__(self, messages: list):
        self.messages = messages

    @staticmethod
    def count_characters(message):
        return len(message)

    def run_tasks(self):
        with ThreadPoolExecutor() as executor:
            character_counts = executor.map(self.count_characters, self.messages)

            return list(character_counts)


def main():
    character_counter = CharacterCounter(messages)
    character_counts = character_counter.run_tasks()

    print(f"Общее количество символов в каждой строке: {character_counts}")


main()
