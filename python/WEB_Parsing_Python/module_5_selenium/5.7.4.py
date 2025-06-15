# 1️⃣ Откройте сайт-тренажёр с помощью Selenium.
# 2️⃣ Найдите среди всех доступных cookie тот, у которого имя (Name) равно "token_22", и извлеките его значение (Value).
# 3️⃣ Вставьте полученное значение из поля value в переменную token_22 = "сюда"
# token_22 = "value_cookie"

from selenium import webdriver
from selenium.webdriver.common.by import By


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/6/6.3.1/index.html"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)

    @staticmethod
    def setup_options():
        from selenium.webdriver.chrome.options import Options

        options = Options()
        # options.add_argument("--headless")  # Без графического интерфейса
        # options.add_argument('--disable-gpu')  # Отключаем GPU
        # options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна

        return options

    def get_result(self, driver, url):

        driver.get(url)
        cookie = driver.get_cookie("token_22")

        return cookie.get("value")

    def run(self):
        with self.driver as driver:
            data = self.get_result(driver, self.url)

            print(data)


def main():
    d = DataDriver()
    d.run()


main()
