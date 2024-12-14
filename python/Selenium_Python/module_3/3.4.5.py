# Точка Входа: Откройте заданный веб-сайт с помощью Selenium.
# Поиск Ссылки: Используйте метод By.PARTIAL_LINK_TEXT или By.LINK_TEXT для поиска ссылки с текстом 16243162441624.
# Клик по Ссылке: Нажмите на найденную ссылку.
# Получение Результата: Скопируйте текст, который появится в теге найденной страницы <p id="result"></p>.
# Фиксация: Запишите полученный результат в отдельную переменную или вставьте ответ в поле ответа степик.

from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://parsinger.ru/selenium/2/2.html"
LINK_TEXT = "16243162441624"


def get_result(url: str, link_text: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        link = driver.find_element(By.PARTIAL_LINK_TEXT, link_text)
        link.click()

        result = driver.find_element(By.ID, "result")
        result_text = result.text

        print(result_text)


get_result(URL, LINK_TEXT)
