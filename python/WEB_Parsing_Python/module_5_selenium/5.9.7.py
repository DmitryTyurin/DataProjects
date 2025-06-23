# 1️⃣ С помощью Selenium зайдите на сайт-тренажер.
# 2️⃣ На главной странице отображается iFrame с вложенным контентом.
# 3️⃣ Выполните следующие действия:
#
# Найдите элемент iFrame и переключитесь в него, используя browser.switch_to.frame().
# Получите HTML-код содержимого iFrame (browser.page_source).
# Извлеките слово, спрятанное между символами * внутри текста.
# (Например, в тексте могут встречаться разбросанные буквы *F*, *s* и т. д. Вам нужно извлечь каждую букву по порядку и соединить их воедино.)
# 4️⃣ Вставьте полученное слово в поле ниже на платформе Stepik.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/8/8.4.1/"
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

        iframe = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframe)
        data = driver.page_source

        code = self.get_code(data)

        return code

    @staticmethod
    def get_code(text: str):
        import re

        hidden_letters = re.findall(r"\*([A-Za-z])\*", text)
        secret_word = "".join(hidden_letters)

        return secret_word

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
