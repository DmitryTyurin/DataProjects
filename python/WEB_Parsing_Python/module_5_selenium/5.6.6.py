# На старт, внимание, марш!: Откройте указанную веб-страницу с помощью Selenium.
# Операция 'Чистый лист': На странице расположены 100 текстовых полей с текстом. Ваша задача — пройтись по каждому и удалить его содержимое. Причём быстро, у вас всего 15 секунд!
# Завершающий этап: После того как все поля будут очищены, нажмите на кнопку на странице.
# Секретный код: Скопируйте число, которое появится во всплывающем alert-окне, с помощью Selenium.
# Результат: Вставьте полученное число в поле ответа степик.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/5.5/1/1.html"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)
        self.alert = Alert(self.driver)

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

        clear_elements = driver.find_elements(By.CLASS_NAME, "text-field")

        [item.clear() for item in clear_elements]

        driver.find_element(By.ID, "checkButton").click()

        result = self.get_alert_text(driver)

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
