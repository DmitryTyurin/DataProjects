# Условие задачи:
# Скачивание файла: Скачайте zip-архив по предоставленной ссылке вручную.
#
# Распаковка архива: Распакуйте этот архив в папку с вашим проектом.
#
# Парсинг HTML: Извлеките содержимое из файла index.html из распакованного архива.
# Для получения ответа используйте lxml парсер.
#
# Вставка содержимого: После извлечения, вставьте полученное содержимое файла в поле ответа.

from bs4 import BeautifulSoup
import lxml

FILE = "index.html"


class DataSoup:
    def __init__(self, file: str):
        self.file = file

    def parse_data(self):
        with open(self.file, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "lxml")
            print(soup)


ds = DataSoup(FILE)
ds.parse_data()
