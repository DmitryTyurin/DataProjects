# 🔹 Задача: На планету Арракис🌕 напали враги.
# Активировать систему экстренной защиты можно лишь по Ключ-Коду🔑 который можно получить нажав кнопку "START" на странице активации системы безопасности.
# Проблема в том, что кнопку можно нажать только через автоматизированное ПО. Помогите жителям планеты, спасите их жизни🕊️.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/3/3.2.1/index.html"
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

        driver.find_element(By.ID, "clickButton").click()
        time.sleep(2)

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
