# Вход в лабиринт: Откройте указанный веб-сайт с помощью Selenium.
# Ключи к сокровищам: Извлеките данные из каждого тега <p> на странице.
# Сложение фрагментов: Просуммируйте все числовые значения, которые вы извлекли.
# Отчет о сокровищах: Запишите сумму в отдельное поле или выведите на экран, полученное значение вставьте в поле ответа степик.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/3/3.html"
        self.driver = webdriver.Chrome()
        self.result_list = []

    def get_result(self, driver, url):
        driver.get(url)

        elements = driver.find_elements(By.TAG_NAME, "p")

        for element in elements:
            digit = int(element.text)
            self.result_list.append(digit)

    def run(self):
        with self.driver as driver:
            self.get_result(driver, self.url)

            print(sum(self.result_list))


def main():
    d = DataDriver()
    d.run()


main()
