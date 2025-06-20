# 1️⃣ Перейдите на сайт-тренажёр с помощью Selenium.
# 2️⃣ Используя метод scroll_by_amount(x, y), прокрутите страницу вниз и считайте код, который появится спустя 3 секунды.
# 3️⃣ Прокрутите страницу ещё раз, введите полученный на предыдущем шаге код и нажмите кнопку «Проверить».
# 4️⃣ Если всё выполнено правильно, появится пароль. Вставьте этот пароль в поле ответа степик.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/7/7.4.1/index.html"
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

        self.action.scroll_by_amount(0, 500).perform()
        time.sleep(5)

        key = driver.find_element(By.CLASS_NAME, "countdown").text
        key = key.split(":")[-1].strip()
        print(key)

        self.action.scroll_by_amount(0, 1500).perform()
        time.sleep(3)

        driver.find_element(By.TAG_NAME, "input").send_keys(key)
        driver.find_element(By.TAG_NAME, "button").click()

        result = driver.find_element(By.ID, "final-key").text
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
