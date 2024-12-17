# На старт, внимание, марш!: Откройте указанную веб-страницу с помощью Selenium.
# Операция 'Чистый Лист': На странице расположены 100 текстовых полей с текстом.
# Ваша задача — пройтись по каждому и удалить его содержимое. Причём быстро, у вас всего 5 секунд!
# Завершающий этап: После того как все поля будут очищены, нажмите на кнопку на странице.
# Секретный Код: Скопируйте число, которое появится во всплывающем alert-окне, с помощью Selenium.
# Результат: Вставьте полученное число в поле ответа степик.


from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://parsinger.ru/selenium/5.5/1/1.html"


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        elements = driver.find_elements(By.CLASS_NAME, "text-field")

        for elem in elements:
            elem.clear()

        checkbox = driver.find_element(By.ID, "checkButton")
        checkbox.click()

        alert = driver.switch_to.alert.text

        print(alert)


get_result(URL)
