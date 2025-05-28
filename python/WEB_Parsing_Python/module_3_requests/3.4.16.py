# Условие:
# Вам предоставлен доступ к API, который возвращает данные в формате JSON.
# Данные представляют собой древовидную структуру переписки между участниками.
# Анализ данных:
#
# Пройдитесь по древовидной структуре переписки.
# Подсчитайте, сколько сообщений отправил каждый участник.
# Участника необходимо определить по полю "username", поле  "user_id" не имеет отношения к решению данной задачи.
# Задача:
# Напишите скрипт, который выполнит GET-запрос к API для получения JSON.
#
# Преобразуйте полученный JSON в Python-объект.
#
# Проанализируйте древовидную структуру переписки и подсчитайте количество сообщений, отправленных каждым участником.
#
# Вставить полученный словарь в поле для ответа.
#
# {'Anastasia': *, 'Vladimir': *, 'Yulia': *, 'Maria': *, 'Kirill': *, 'Anton': *, 'Petr': *, 'Dmitry': *, 'Olga': *, 'Maxim': *, 'Elena': *, 'Alex': *, 'Natalia': *, 'Tatiana': *, 'Svetlana': *, 'Andrey': *, 'Sergey': *, 'Oksana': *, 'Ivan': *, 'Irina': *}
# Сортировка:
# Необходимо упорядочить данный словарь сначала по убыванию числа сообщений. То есть участник с наибольшим количеством сообщений должен идти первым, а с наименьшим — последним.
# В случае равенства числа сообщений между участниками, необходимо применить дополнительный критерий сортировки. Этот критерий основан на лексикографическом порядке имен участников. Лексикографическая сортировка схожа с алфавитной: если, например, имена 'Алексей' и 'Анна' имеют одинаковое количество сообщений, то 'Алексей' будет расположен перед 'Анной', так как лексикографически он идет раньше. Таким образом, участники с одинаковым числом сообщений будут упорядочены в словаре в зависимости от их имён, начиная с самого раннего и заканчивая самым поздним.
#
# Пример ниже не является корректным для системы проверки:
# {'Vladimir': 21, 'Yulia': 21, 'Anton': 14, 'Kirill': 14, 'Petr': 14, 'Dmitry': 8, 'Elena': 8, 'Maxim': 8, 'Olga': 8, 'Alex': 6, 'Natalia': 6, 'Svetlana': 6, 'Tatiana': 6, 'Oksana': 5, 'Sergey': 5}
# В примере выше:
# У 'Vladimir' и 'Yulia' одинаковое количество сообщений —21. В лексикографическом порядке "Vladimir" идет раньше "Yulia", поэтому он идет первым.
#
# 'Anton', 'Kirill', и 'Petr' имеют по 14 сообщений. В лексикографическом порядке имена располагаются так: 'Anton', 'Kirill', 'Petr'.
#
# и т.д

import requests

URL = "https://parsinger.ru/3.4/3/dialog.json"


class DataRequests:
    def __init__(self, url):
        self.url = url
        self.user_message_count = {}

    def get_data(self):
        try:
            response = requests.get(self.url)

            if response.encoding != "utf-8":
                response.encoding = "utf-8"

            response.raise_for_status()

            return response.json()

        except Exception as e:
            print(e)
            return None

    def traverse_comments(self, comments):
        for comment in comments:
            username = comment["username"]

            if username not in self.user_message_count:
                self.user_message_count[username] = 0
            self.user_message_count[username] += 1

            if "comments" in comment and len(comment["comments"]) > 0:
                self.traverse_comments(comment["comments"])

    def count_messages(self, comment_tree):
        self.traverse_comments([comment_tree])

        return self.user_message_count

    @staticmethod
    def get_sorted_data(message_counts):

        return dict(sorted(message_counts.items(), key=lambda x: (-x[1], x[0])))

    def get_results(self):
        import json

        # Получение данных из API и преобразование их в Python-объект
        data = self.get_data()

        # Подсчет количества сообщений от каждого участника
        user_message_count = self.count_messages(data)

        # Сортировка словаря по убыванию числа сообщений и лексикографическому порядку имен участников
        sorted_user_message_count = self.get_sorted_data(user_message_count)

        # Преобразование словаря в JSON-строку с отступами и корректным отображением русских символов
        json_data = json.dumps(sorted_user_message_count, indent=4, ensure_ascii=False)

        return sorted_user_message_count


data_requests = DataRequests(URL)

results = data_requests.get_results()
print(results)
