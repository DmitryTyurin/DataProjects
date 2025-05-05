# Вы - опытный разработчик, которому доверено исправить критическую задачу, возникшую из-за недочетов новичка Александра. Ваша работа имеет решающее значение для проекта, и от вашей скорости, точности и умения работать с многопоточностью зависит успех всего задания.
#
# Цели и Задачи:
# Новичок Александр, недавно принятый на работу, не смог выполнить задачу по формированию файла JSON, как того требовали. Вам, как самому опытному разработчику, предстоит исправить ошибки и довести работу до конца.
# Данные, полученные Александром уже загружены с сервера и разбросаны по десяти различным файлам. Вы должны написать многопоточный код, который соберет данные из всех десяти файлов в один JSON файл, не забудьте про блокировки мьютекса lock().
# Архив с необходимыми для задания файлами находится тут.
# #Имена файлов, они же ключи в итоговом json.
#
# first_name.txt
# last_name.txt
# age.txt
# country.txt
# hobbies.txt
# salary.txt
# job_title.txt
# email.txt
# projects.txt
# education.txt
#
#
# Вам необходимо извлекать по одной строке из каждого файла одновременно и формировать из них объекты JSON, где ключи — это названия файлов без расширения .txt, а значения — соответствующие строки из каждого файла.
# Примеры объектов JSON приведены в вашем задании.
# [
# # Первый сформированный словарь в файле
#     {
#         "first_name": "Amanda",
#         "last_name": "Reese",
#         "age": "33",
#         "country": "Guinea-Bissau",
#         "hobbies": "us",
#         "salary": "71207$",
#         "job_title": "Human resources officer",
#         "email": "stewartdavid@example.net",
#         "projects": "Treat Mrs value sure special draw receive. Some music practice example particularly building. Indicate note church add beat type all.",
#         "education": "Mr today black public take research couple. Image help performance agree."
#     },
#
# ...
# ...
# ...
#
# # Последний сформированный словарь в файле
#     {
#         "first_name": "Victor",
#         "last_name": "Ramos",
#         "age": "57",
#         "country": "Puerto Rico",
#         "hobbies": "history",
#         "salary": "32485$",
#         "job_title": "Logistics and distribution manager",
#         "email": "ashley04@example.com",
#         "projects": "But think behind. Several could leg issue. Cup money fight reveal next support. Wish group once collection what.",
#         "education": "Available person whom center standard special message. Necessary or beat spring."
#     }
# ]
# После создания JSON файла, используйте валидатор по этой ссылке для проверки корректности файла. Успешное прохождение валидации даст вам секретный код, который необходимо будет использовать для подтверждения выполнения задачи на степик.
# Вам необходимо использовать архив с файлами, предоставленный по ссылке, где каждый файл содержит 5000 строк. В результате, ваш итоговый JSON файл должен содержать 5000 словарей.
# Порядок ключей в словаре должен соответствовать примеру выше.

from concurrent.futures import ThreadPoolExecutor
import threading
import time
import json


class JsonExtractor:
    def __init__(self):
        self.file_path = ""
        self.file_names = [
            "first_name.txt",
            "last_name.txt",
            "age.txt",
            "country.txt",
            "hobbies.txt",
            "salary.txt",
            "job_title.txt",
            "email.txt",
            "projects.txt",
            "education.txt",
        ]
        self.files_data = [
            f"{self.file_path}/{file_name}" for file_name in self.file_names
        ]
        self.json_data = {}
        self.lock = threading.Lock()
        self.executor = ThreadPoolExecutor(max_workers=32)

    def extract_data(self, file):
        with self.lock:
            with open(file, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for i, line in enumerate(lines):
                    file = file.replace(".txt", "").replace(f"{self.file_path}/", "")
                    line = line.replace("\n", "")

                    if i not in self.json_data:
                        self.json_data[i] = {}

                    self.json_data[i][file] = line.strip()

    def run_executor(self):
        with self.executor as executor:
            futures = [
                executor.submit(self.extract_data, file_name)
                for file_name in self.files_data
            ]

    def load_data(self):
        self.run_executor()

        with open("output.json", "w") as f:
            json.dump(list(self.json_data.values()), f, indent=4, ensure_ascii=False)


extractor = JsonExtractor()
extractor.load_data()
