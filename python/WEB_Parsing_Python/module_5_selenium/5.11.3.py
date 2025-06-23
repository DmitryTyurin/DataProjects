# 1️⃣ С помощью Selenium зайдите на сайт-тренажёр.
# 2️⃣ Нажмите кнопку "INITIATE SCAN" для запуска сканирования.
# 3️⃣ Title страницы начнёт динамически изменяться (пример: "Scanning..." → "Processing..." → "Access Granted").
# 4️⃣ Используйте WebDriverWait с title_is("Access Granted"), чтобы дождаться нужного заголовка.
# 5️⃣ Как только title изменится на "Access Granted", пароль появится на странице.
# 6️⃣ Считайте пароль из DOM и вставьте его в поле ниже на Stepik.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/9/9.2.1/index.html"
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

        scan_button = driver.find_element(By.ID, "startScan")
        scan_button.click()

        WebDriverWait(driver, 30).until(EC.title_is("Access Granted"))

        result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
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
