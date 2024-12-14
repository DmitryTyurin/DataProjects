# Вход в Лабиринт: Откройте указанный веб-сайт с помощью Selenium.
# Ключи к Сокровищам: Извлеките данные из каждого тега <p> на странице.
# Сложение Фрагментов: Просуммируйте все числовые значения, которые вы извлекли.
# Отчет о Сокровищах: Запишите сумму в отдельное поле или выведите на экран, полученное значение вставьте в поле ответа степик.

from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://parsinger.ru/selenium/3/3.html"


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        elements = driver.find_elements(By.TAG_NAME, "p")

        result = 0
        for elem in elements:
            n = int(elem.text)
            result += n

        print(result)


get_result(URL)
