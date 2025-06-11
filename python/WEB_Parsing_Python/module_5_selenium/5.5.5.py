# 1️⃣ Зайдите на сайт-тренажер с помощью Selenium.
# 2️⃣ Найдите кнопку по id со значением "secret-key-button".
# 3️⃣ Кликните по кнопке.
# 4️⃣ Извлеките значение атрибута data с помощью метода .get_attribute("data").
# 5️⃣ Вставьте полученный ключ в поле ниже между кавычек.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/3/3.2.4/index.html"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)

    @staticmethod
    def setup_options():
        from selenium.webdriver.chrome.options import Options

        options = Options()
        # options.add_argument("--headless")  # Без графического интерфейса
        # options.add_argument('--disable-gpu')  # Отключаем GPU
        options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна

        return options

    @staticmethod
    def get_result(driver, url):
        driver.get(url)

        element = driver.find_element(By.ID, "secret-key-button")
        element.click()

        return element.get_attribute("data")

    def run(self):
        with self.driver as driver:
            data = self.get_result(driver, self.url)

            print(data)


def main():
    d = DataDriver()
    d.run()


main()
