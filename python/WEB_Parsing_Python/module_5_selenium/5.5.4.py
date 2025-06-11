# 1️⃣ Зайдите на сайт-тренажер с помощью Selenium.
# 2️⃣ Нажмите кнопку "Начать миссию".
# 3️⃣ Получите пароль, который появится на экране (с помощью метода .text).
# 4️⃣ Введите этот пароль в поле и нажмите кнопку "Проверить".
# 5️⃣ Если пароль правильный, появится финальный ключ. Его нужно извлечь из элемента с id="text2". И вставить здесь в поле ниже между кавычек.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/3/3.2.3/index.html"
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

        driver.find_element(By.ID, "showTextBtn").click()
        password = driver.find_element(By.ID, "text1").text

        driver.find_element(By.ID, "userInput").send_keys(password)
        driver.find_element(By.ID, "checkBtn").click()

        result = driver.find_element(By.ID, "text2").text

        return result

    def run(self):
        with self.driver as driver:
            data = self.get_result(driver, self.url)

            print(data)


def main():
    d = DataDriver()
    d.run()


main()
