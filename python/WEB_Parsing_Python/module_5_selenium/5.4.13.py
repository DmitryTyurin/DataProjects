# Взлом кодового замка: Откройте веб-сайт с помощью Selenium.
# Активация чек-боксов: Найдите все чек-боксы на странице и установите их в положение checked с помощью .click().
# Открывание секрета: Как только все чек-боксы будут активированы, нажмите на кнопку.
# Доступ к секретным данным: Скопируйте число, которое появится в теге <p id="result">Result</p>.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/4/4.html"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)

    @staticmethod
    def setup_options():
        from selenium.webdriver.chrome.options import Options

        options = Options()
        options.add_argument("--headless")  # Без графического интерфейса
        # options.add_argument('--disable-gpu')  # Отключаем GPU
        # options.add_argument('--window-size=1920,1080')  # Устанавливаем размер окна

        return options

    @staticmethod
    def get_result(driver, url):
        driver.get(url)

        elements = driver.find_elements(By.CLASS_NAME, "check")

        for element in elements:
            element.click()

        button = driver.find_element(By.CLASS_NAME, "btn").click()
        result = driver.find_element(By.ID, "result").text

        return result

    def run(self):
        with self.driver as driver:
            data = self.get_result(driver, self.url)

            print(data)


def main():
    d = DataDriver()
    d.run()


main()
