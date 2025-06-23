# 1️⃣ С помощью Selenium зайдите на сайт-тренажёр.
# 2️⃣ На странице находятся 5 кнопок, первые 4 из которых активируется через случайный промежуток времени.
# 3️⃣ Используйте WebDriverWait, чтобы дождаться активации каждой кнопки и нажать её.
# 4️⃣ Финальная кнопка станет активной после нажатия всех предыдущих и откроет секретный пароль.
# 5️⃣ Считайте пароль и вставьте его в поле ниже на платформе Stepik.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/9/9.1.1/index.html"
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

        for i in range(1, 5):
            button_locator = (By.ID, f"button{i}")
            button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(button_locator)
            )
            button.click()

        final_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "finalButton"))
        )
        final_button.click()

        result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "message"))
        )
        result = result.text
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
