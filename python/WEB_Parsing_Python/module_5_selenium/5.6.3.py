# 1️⃣ Зайти на сайт-тренажёр с помощью Selenium.
# 2️⃣ Найти картинку с id="this_pic"
# 3️⃣ Сделать скриншот картинки.
# 4️⃣ На ней будет код, который вам нужно будет ввести здесь в поле ниже.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/6/6.2.1/index.html"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)
        self.alert = Alert(self.driver)
        self.result = []

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

        element = driver.find_element(By.ID, "this_pic")
        element.screenshot("image.png")

    def run(self):
        with self.driver as driver:
            self.get_result(driver, self.url)


def main():
    d = DataDriver()
    d.run()


main()
