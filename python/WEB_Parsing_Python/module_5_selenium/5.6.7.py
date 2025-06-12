# Стартовая gозиция: Используя Selenium, откройте заданный веб-сайт. Убедитесь, что ваша машина готова к операции.
# Секунды на cчетчике: У вас есть ровно 10 секунд, чтобы пройтись по ячейкам на странице и очистить только те, которые доступны для редактирования.
# Проверка: Нажмите на кнопку "Проверить" на странице.
# Секретный код: Из всплывающего алерт-окна скопируйте код и вставьте его в поле для ответа.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/5.5/2/1.html"
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

        [
            item.clear()
            for item in clear_elements
            if item.get_attribute("disabled") is None
        ]

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
