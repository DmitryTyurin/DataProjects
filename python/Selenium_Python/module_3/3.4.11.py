# Откройте Таинственную Страницу: Используя Selenium, откройте веб-страницу, где хранится первая подсказка.
# Решение Загадки: Найдите значение математического уравнения.
# Ключ к Выпадающему Списку: Откройте выпадающий список и выберите элемент с числом, которое у вас получилось на предыдущем этапе.
# Активация Механизма: Нажмите на кнопку на странице, если значение верное, вы получите код.
# Завершение Миссии: Скопируйте число, которое появится на странице после нажатия на кнопку, и вставьте его в поле ответа степик.

from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://parsinger.ru/selenium/6/6.html"


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        num = driver.find_elements(By.ID, "text_box")
        magic_key = eval(num[0].text)

        all_keys = driver.find_elements(By.TAG_NAME, "option")
        for i in all_keys:
            if int(i.text) == magic_key:
                i.click()

        driver.find_element(By.CLASS_NAME, "btn").click()
        result = driver.find_element(By.ID, "result").text

        print(result)


get_result(URL)
