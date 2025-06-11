# Основные этапы
# Точка входа: Откройте заданный веб-сайт с помощью Selenium.
# Поиск ссылки: Используйте метод By.PARTIAL_LINK_TEXT или By.LINK_TEXT для поиска ссылки с текстом 16243162441624.
# Клик по ссылке: Нажмите на найденную ссылку.
# Получение результата: Скопируйте текст, который появится в теге найденной страницы <p id="result"></p>.
# Фиксация: Запишите полученный результат в отдельную переменную или вставьте ответ в поле ответа степик.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/2/2.html"
        self.driver = webdriver.Chrome()
        self.link_text = "16243162441624"

    def get_result(self, driver, url):
        driver.get(url)

        driver.find_element(By.PARTIAL_LINK_TEXT, self.link_text).click()

        return driver.find_element(By.ID, "result").text

    def run(self):
        with self.driver as driver:
            result = self.get_result(driver, self.url)

            print(result)


def main():
    d = DataDriver()
    d.run()


main()
