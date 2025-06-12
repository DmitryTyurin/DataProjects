# Открыть страницу тренажёра набора текста
# Определить тег для текущего символа, который необходимо ввести
# Корректно обрабатывать все символы в тексте
# Последовательно вводить символы до завершения упражнения
# Получить и вставить секретный код, который появится по окончании задания

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/5.6/3/index.html"
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
        actions = ActionChains(driver)

        while True:
            current_char = driver.find_element(By.CLASS_NAME, "current-char").text

            if current_char == "⎵":
                actions.send_keys(Keys.SPACE).perform()
            else:
                actions.send_keys(current_char).perform()

            try:
                secret_code_element = driver.find_element(By.ID, "secret-code")
                result = secret_code_element.text
                if result:
                    return result
            except:
                continue

    def run(self):
        with self.driver as driver:
            data = self.get_result(driver, self.url)

            print(data)


def main():
    d = DataDriver()
    d.run()


main()
