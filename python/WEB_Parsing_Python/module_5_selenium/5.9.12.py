# 1️⃣ С помощью Selenium зайдите на сайт-тренажер.
# 2️⃣ Установите размер окна браузера на 1200×720
# 3️⃣ Нажмите на кнопку "Проверить размер". Если размеры окна установлены корректно (с учетом допустимого отклонения), на странице появится скрытый пароль.
# 4️⃣ Считайте из DOM полученный пароль.
# 5️⃣ Вставьте пароль в поле ниже на степик.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/8/8.2.1/index.html"
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

        driver.set_window_size(1200, 720)
        driver.find_element(By.ID, "checkSizeBtn").click()
        result = driver.find_element(By.ID, "secret").text

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
