# 🔹 Задача: Пробраться сквозь лабиринт вложенных iframes и добыть секретный пароль в виде фразы, которую произносят вновь прибывшие при посвящении в адепты iframe!
#
# 1️⃣ Запустите Selenium и откройте сайт-тренажёр.
# 2️⃣ На главной странице расположен iframe 1. Переключитесь в iframe 1 с помощью .switch_to.frame(...) и нажмите кнопку. Внутри iframe 1 динамически погрузится iframe 2.
# 3️⃣ Повторите действия, добравшись до iframe 4. В iframe 4 спрятан пароль. Найдите его и заберите! 🏆
# 4️⃣ Считайте фразу-пароль и вставьте её в поле ниже на платформе Stepik.
# 🟢 Внимание: Пароль отобразится только при использовании Selenium.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/8/8.4.3/index.html"
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
            iframe = driver.find_element(By.TAG_NAME, "iframe")
            driver.switch_to.frame(iframe)
            driver.find_element(By.CLASS_NAME, "button").click()

        result = driver.find_element(By.CLASS_NAME, "password-container").text
        # result = result.split(":")[-1].strip()

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
