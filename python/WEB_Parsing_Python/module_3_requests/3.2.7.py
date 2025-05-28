# Напишите программу, которая выполнит GET-запрос и выведет основные сведения о полученном ответе.
#
# Отправьте GET-запрос на url и сохраните результат в переменную response.
# Выведите в консоль (в указанном порядке) и вставьте полученное содержимое в поля ниже:
# response.status_code   # числовой код ответа сервера
# response.text          # тело ответа
# response.headers       # словарь HTTP-заголовков
# response.cookies       # объект cookies

import requests

# Отправляем GET-запрос
url = "https://parsinger.ru/selenium/6/6.3.1/index.html"
response = requests.get(url)
response.encoding = "utf-8"

# Выводим требуемые данные
print("Status code:", response.status_code)
print("Response text:", response.text)
print("Headers:", response.headers)
print("Cookies:", response.cookies)
