# Откройте таинственную страницу: Используя Selenium, откройте веб-страницу, где хранится первая подсказка.
# Решение загадки: Вычислите значение математического выражения.
# Ключ к выпадающему списку: Откройте выпадающий список и выберите элемент с числом, которое у вас получилось на предыдущем этапе.
# Завершение миссии: Скопируйте число, которое появится на странице после нажатия на кнопку, и вставьте его в поле ответа степик.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/6/6.html"
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

        mat_expressions = eval(driver.find_elements(By.ID, "text_box")[0].text)
        elements = driver.find_elements(By.TAG_NAME, "option")

        for element in elements:
            digit = int(element.text)

            if digit == mat_expressions:
                element.click()
                break

        driver.find_element(By.CLASS_NAME, "btn").click()

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
