# 🔹 Задача: Вы стоите перед магической дверью, которая ведёт в другой мир. Чтобы открыть её, нужно произнести имя самого могущественного дракона🐉 Дейенерис Таргариен.
# Зайдите на сайт-тренажер и введите имя её самого большого и сильного дракона, чтобы получить ключ. Этот ключ нужно ввести здесь, в поле ниже между кавычками.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/3/3.2.2/index.html"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)
        self.name = "Дрогон"

    @staticmethod
    def setup_options():
        from selenium.webdriver.chrome.options import Options

        options = Options()
        # options.add_argument("--headless")  # Без графического интерфейса
        # options.add_argument('--disable-gpu')  # Отключаем GPU
        options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна

        return options

    def get_result(self, driver, url):
        driver.get(url)

        driver.find_element(By.ID, "codeInput").send_keys(self.name)
        driver.find_element(By.ID, "clickButton").click()
        time.sleep(10)

        result = driver.find_element(By.ID, "codeOutput").text

        return result

    def run(self):
        with self.driver as driver:
            data = self.get_result(driver, self.url)

            print(data)


def main():
    d = DataDriver()
    d.run()


main()
