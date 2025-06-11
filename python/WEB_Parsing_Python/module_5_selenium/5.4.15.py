# Вход в кодовую комнату: Откройте сайт с помощью Selenium.
# Извлечение ключей: Получите значения всех элементов выпадающего списка.
# Дешифровка кода: Сложите (плюсуйте) все извлеченные значения.
# Использование кода: Вставьте получившийся результат в поле на сайте и нажмите кнопку.
# Получение конечного результата: Копируйте длинное число, которое появится после нажатия на кнопку.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/7/7.html"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)

    @staticmethod
    def setup_options():
        from selenium.webdriver.chrome.options import Options

        options = Options()
        # options.add_argument("--headless")  # Без графического интерфейса
        # options.add_argument('--disable-gpu')  # Отключаем GPU
        # options.add_argument('--window-size=1920,1080')  # Устанавливаем размер окна

        return options

    @staticmethod
    def get_result(driver, url):
        driver.get(url)

        elements = driver.find_elements(By.TAG_NAME, "option")
        sum_elements = sum([int(item.text) for item in elements])

        driver.find_element(By.ID, "input_result").send_keys(sum_elements)
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
