# Вооружитесь браузером и пусть ваш код проникнет на сайт.
# Поиск секретных cookies: Найдите все скрытые secret_cookie_, которые могут содержать важную информацию
# Дешифровка и анализ: Суммируйте числовые значения всех secret_cookie_.
# Это может быть частью шифра или ключом к следующему уровню.
# Ввод ответа: Вставьте полученную сумму в поле ответа степик.
# Это ваш ключ к успешному завершению миссии.

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://parsinger.ru/methods/3/index.html"

# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome(options_chrome) as driver:
        driver.get(url)

        cookies = driver.get_cookies()
        result = 0

        for cookie in cookies:
            result += int(cookie.get("value"))

        print(result)


get_result(URL)
