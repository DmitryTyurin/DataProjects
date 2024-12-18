# Стартовая Позиция: Используя Selenium, откройте заданный веб-сайт.
# Убедитесь, что ваша машина готова к операции.
# Секунды на Счетчике: У вас есть ровно 5 секунд, чтобы пройтись по ячейкам на странице и очистить только те, которые доступны для редактирования.
# Проверка: Нажмите на кнопку "Проверить" на странице.
# Секретный код: Из всплывающего алерт-окна скопируйте код и вставьте его в поле для ответа.


from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://parsinger.ru/selenium/5.5/2/1.html"


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        text_fields = driver.find_elements(By.TAG_NAME, "input")

        for field in text_fields:
            if field.get_attribute("disabled") is None:
                field.clear()

        check_button = driver.find_element(By.ID, "checkButton")
        check_button.click()

        alert = driver.switch_to.alert.text

        print(alert)


get_result(URL)
