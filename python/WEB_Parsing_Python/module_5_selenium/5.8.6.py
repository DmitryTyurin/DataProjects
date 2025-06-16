# Стартовая позиция: Запустите Selenium и откройте данный веб-сайт. Убедитесь, что ваша станция готова к операции.
#
# Сбор урана: Пройдитесь по каждому кусочку урана на странице и кликните по нему. Это поможет нам вернуть его обратно на корабль.
#
# #Подсказка
# driver.execute_script("return arguments[0].scrollIntoView(true);", button)
# Получение секретного кода: Как только в открытом космосе не останется ни одного кусочка урана, команда пришлёт вам в alert-окне секретный код.
#
# #Подсказка
# alert_text = alert.text
# Финальный этап: Вставьте полученный секретный код в необходимое поле для завершения операции.


from selenium import webdriver
from selenium.webdriver.common.by import By


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/5.7/1/index.html"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)

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

        element = driver.find_elements(By.CLASS_NAME, "clickMe")

        for element in element:
            driver.execute_script("arguments[0].scrollIntoView();", element)
            element.click()

        result = self.get_alert_text(driver)

        return result

    @staticmethod
    def get_alert_text(driver):
        alert_text = None

        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
        except Exception as e:
            print(f"Всплывающее окно не найдено: {e}")

        return alert_text

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
