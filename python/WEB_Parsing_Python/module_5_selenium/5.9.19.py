# С помощью Selenium запустите сначала браузер с пустой вкладкой about:blank.
# Используйте метод .new_window("tab") откройте сайт 1 в новой вкладке.
# Получите из title числовое значение, затем удалите из него все числа 4, 3, 9,  сохраните обработанное число в num1.
# Откройте сайт 2 в новой вкладке тем же методом.
# Получите из title числовое значение, затем удалите из него все числа 7, 8, 0,  сохраните обработанное число в num2.
# Суммируйте полученные ранее числа num1 + num2, полученное значение вставьте в поле ниже на степик.
# ❗Внимание title доступен только через Selenium.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/8/8.1/"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)
        self.action = ActionChains(self.driver)
        self.default_size = 555

    @staticmethod
    def setup_options():
        from selenium.webdriver.chrome.options import Options

        options = Options()
        # options.add_argument("--headless")  # Без графического интерфейса
        # options.add_argument('--disable-gpu')  # Отключаем GPU
        options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна

        return options

    def get_result(self, driver, url):
        import time

        driver.get("about:blank")

        driver.switch_to.new_window("tab")
        driver.get(f"{self.url}/site1")
        title_site1 = driver.title
        num1 = self.get_number(title_site1, ["4", "3", "9"])

        driver.switch_to.new_window("tab")
        driver.get(f"{self.url}/site2")
        title_site1 = driver.title
        num2 = self.get_number(title_site1, ["7", "8", "0"])

        return num1 + num2

    @staticmethod
    def get_number(title, digits_to_remove):
        raw_number = "".join(filter(str.isdigit, title))

        processed_number = "".join(
            digit for digit in raw_number if digit not in digits_to_remove
        )

        return int(processed_number) if processed_number else 0

    def run(self):
        with self.driver as driver:
            data = self.get_result(driver, self.url)

            print(data)


def main():
    import time

    start_time = time.perf_counter()

    d = DataDriver()
    d.run()

    end_time = time.perf_counter()

    print(f"Время выполнения: {end_time - start_time:.2f} секунд")


main()
