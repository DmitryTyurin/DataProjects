# Вход в Кодовую Комнату: Откройте сайт с помощью Selenium.
# Извлечение Ключей: Получите значения всех элементов выпадающего списка.
# Дешифровка Кода: Сложите (плюсуйте) все извлеченные значения.
# Использование Кода: Вставьте получившийся результат в поле на сайте и нажмите кнопку.
# Получение Конечного Результата: Копируйте длинное число, которое появится после нажатия на кнопку.

from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://parsinger.ru/selenium/7/7.html"


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        link = driver.find_elements(By.TAG_NAME, "option")

        sum_item = sum([int(i.text) for i in link])

        driver.find_element(By.ID, "input_result").send_keys(sum_item)
        driver.find_element(By.CLASS_NAME, "btn").click()
        result = driver.find_element(By.ID, "result").text

        print(result)


get_result(URL)
