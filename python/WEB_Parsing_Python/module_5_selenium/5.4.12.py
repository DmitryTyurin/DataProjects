# Вход в цифровой лабиринт: Используйте Selenium для открытия указанного веб-сайта.
# Извлечение фрагментов: Найдите и извлеките данные из каждого второго тега <p> на странице.
# Воссоздание артефакта: Просуммируйте все числовые значения, полученные из этих тегов.
# Ключ к загадке: Запишите полученную сумму в предназначенное для этого поле или выведите на экран.

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

        elements = driver.find_elements(By.XPATH, "//div[@class='text']/p[2]")

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
