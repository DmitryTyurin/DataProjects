# Место преступления: Откройте указанный сайт с помощью Selenium.
# Улики на месте: На сайте вы найдете список пин-кодов. Однако среди них лишь один правильный.
# Расшифровка: Для проверки каждого пин-кода используйте кнопку "Проверить". При верном пин-коде вы получите секретный код.
# Доклад о проведенной работе: Вставьте полученный секретный код в специальное поле для ответа на этой странице.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/8/8.4.2/index.html"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)
        self.action = ActionChains(self.driver)
        self.pins = []

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

        driver.get(url)

        for i in range(1, 4):
            iframe = driver.find_element(By.ID, f"frame{i}")
            driver.switch_to.frame(iframe)
            driver.find_element(By.CLASS_NAME, "unlock-button").click()
            driver.switch_to.default_content()

        iframe = driver.find_element(By.ID, f"frame4")
        driver.switch_to.frame(iframe)

        result = driver.find_element(By.XPATH, "//h2").text
        result = result.split(":")[-1].strip()

        return result

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
