# Цель
# Доступ к месту преступления: Используйте Selenium, чтобы получить доступ к веб-сайту, где спрятаны улики.
# Внимательное расследование: На сайте находится 100 кнопок. Каждая из них при нажатии активирует всплывающее alert окно с пин-кодом.
# Расшифровка: Под кнопками расположено текстовое поле, которое проверяет пин-коды. Ваша задача — ввести пин-код и проверить его. Если пин-код верный, вы получите секретный код.
# Завершение задачи: Вставьте полученный секретный код в специальное поле для ответа на степик.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/5.8/2/index.html"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)
        self.action = ActionChains(self.driver)

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

        buttons = driver.find_elements(By.CLASS_NAME, "buttons")

        for button in buttons:
            button.click()

            code = driver.switch_to.alert.text
            driver.switch_to.alert.accept()

            driver.find_element(By.ID, "input").send_keys(code)
            driver.find_element(By.ID, "check").click()

            result = driver.find_element(By.ID, "result").text

            if result != "Неверный пин-код":
                break

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
