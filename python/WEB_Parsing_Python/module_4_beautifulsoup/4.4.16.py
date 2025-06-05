# Проанализируйте предоставленный HTML-код страницы. Ваша задача - обнаружить и извлечь все email-адреса, которые находятся вне стандартных тегов.
# Вам предстоит модифицировать функцию ниже таким образом, чтобы она возвращала список всех найденных email-адресов, очищенных от лишних пробелов с помощью метода strip().
# Ваша функция должна возвращать список email-адресов в чистом виде, готовых к дальнейшему использованию.
# Пример:
# ['keep2036@duck.com', 'andrea1837@example.org', и т.д.,]

from bs4 import BeautifulSoup
import requests

URL = "https://parsinger.ru/4.1/1/index5.html"


class DataSoup:
    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup(self.get_html(), "lxml")

    def get_html(self):
        response = requests.get(self.url)
        response.encoding = "utf-8"

        response.raise_for_status()

        if response.status_code == 200:
            return response.text
        else:
            return None

    @staticmethod
    def extract_email(text):
        import re

        pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        emails = "".join(re.findall(pattern, text))

        return emails

    def get_data(self):

        data = self.soup.find_all(attrs={"class": "email_field"})
        result = [self.extract_email(item.get_text(strip=True)) for item in data]

        return result


def main():
    ds = DataSoup(URL)
    print(ds.get_data())


main()
