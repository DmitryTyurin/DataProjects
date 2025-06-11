# 1️⃣ Зайти на сайт-тренажёр с помощью Selenium.
# 2️⃣ Найти все элементы с class="block".
# 3️⃣ Пройтись по каждому элементу в цикле и кликнуть кнопку.
# 4️⃣ После того как все кнопки будут нажаты, появится заветный пароль в теге <password> — считать его с помощью .text.
# 5️⃣ Вставить полученный пароль в поле ниже, между кавычек.


from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/3/3.3.2/index.html"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)
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

        elements = driver.find_elements(By.CLASS_NAME, "block")

        for element in elements:
            element.find_element(By.CLASS_NAME, "button").click()

        result = driver.find_element(By.TAG_NAME, "password").text

        return result

    def run(self):
        with self.driver as driver:
            data = self.get_result(driver, self.url)

            print(data)


def main():
    d = DataDriver()
    d.run()


main()
