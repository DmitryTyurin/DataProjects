# 1️⃣ Зайти на сайт-тренажёр с помощью Selenium.
# 2️⃣ Перейти по ссылке на страницу 2.
# 3️⃣ Перейти по ссылке на страницу 3.
# 4️⃣ Используя метод back(), вернуться на первую страницу и кликнуть по кнопке "Показать код".
# 5️⃣ Пока что вручную скопировать код и вставить его сюда в поле ниже. Позже мы изучим, как работать с Alert окнами с

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/6/6.2/index.html"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)
        self.alert = Alert(self.driver)
        self.result = []

    @staticmethod
    def setup_options():
        from selenium.webdriver.chrome.options import Options

        options = Options()
        # options.add_argument("--headless")  # Без графического интерфейса
        # options.add_argument('--disable-gpu')  # Отключаем GPU
        options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна

        return options

    def get_result(self, driver, url):
        driver.get(url)

        [driver.find_element(By.TAG_NAME, "a").click() for i in range(2)]

        [driver.back() for i in range(2)]

        driver.find_element(By.ID, "getPasswordBtn").click()

        result = self.get_alert_text(driver).split(":")[1].strip()

        return result

    @staticmethod
    def get_alert_text(driver):
        alert = None
        alert_text = None

        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
        except Exception as e:
            print(f"Всплывающее окно не найдено: {e}")
        finally:
            if alert:
                alert.accept()

        return alert_text

    def run(self):
        with self.driver as driver:
            data = self.get_result(driver, self.url)

            print(data)


def main():
    d = DataDriver()
    d.run()


main()
