# 1️⃣ С помощью Selenium зайдите на сайт-тренажер.
# 2️⃣ Получите размеры окна браузера.
# 3️⃣ Сложите значения.
# 4️⃣ Введите полученную сумму в поле на сайте тренажере и нажмите кнопку «Проверить».
# 5️⃣ Если ответ верный (с учетом небольшого допуска), на странице отобразится секретный пароль.
# 6️⃣ Вставьте пароль в поле ниже на степик.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/8/8.2.2/index.html"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)
        self.action = ActionChains(self.driver)
        self.codes = []

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

        height = driver.get_window_size().get("height")
        width = driver.get_window_size().get("width")

        size = height + width

        driver.find_element(By.ID, "answer").send_keys(size)
        driver.find_element(By.ID, "checkBtn").click()

        result = driver.find_element(By.ID, "resultMessage").text
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
