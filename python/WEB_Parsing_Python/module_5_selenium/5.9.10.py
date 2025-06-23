# Погружение в кибермир: Используя Selenium, перейдите на указанный сайт.
# Поиск зеркальных комнат: На сайте вы обнаружите 9 iframe. В каждом из них скрыта кнопка.
# Сбор информации: Нажмите на кнопку в каждом iframe, чтобы получить число. Но помните, с вероятностью 1/9 это число окажется тем самым ключом к сейфу.
# Открытие тайны: Вставьте полученное число в поле для проверки. Если удача на вашей стороне, то это число откроет перед вами секретный код в alert.
# Вставьте полученный код из alert в поле ответа степик.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/5.8/5/index.html"
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

        input_btn = driver.find_element(By.ID, "guessInput")
        check_btn = driver.find_element(By.ID, "checkBtn")

        iframes = driver.find_elements(By.TAG_NAME, "iframe")

        for i in iframes:
            driver.switch_to.frame(i)
            driver.find_element(By.TAG_NAME, "button").click()
            number = driver.find_element(By.ID, "numberDisplay").text

            self.codes.append(number)
            driver.switch_to.default_content()

        for code in self.codes:
            input_btn.clear()
            input_btn.send_keys(code)
            check_btn.click()

        result = driver.switch_to.alert.text

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
