# 1️⃣ Зайти на сайт-тренажёр с помощью Selenium.
# 2️⃣ Удалить все cookies, появится пароль.
# 3️⃣ Вставить пароль в поле ниже, между кавычками.

from selenium import webdriver
from selenium.webdriver.common.by import By


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/6/6.3.2/index.html"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)

    @staticmethod
    def setup_options():
        from selenium.webdriver.chrome.options import Options

        options = Options()
        # options.add_argument("--headless")  # Без графического интерфейса
        # options.add_argument('--disable-gpu')  # Отключаем GPU
        # options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна

        return options

    def get_result(self, driver, url):
        import time

        driver.get(url)

        driver.delete_all_cookies()
        time.sleep(3)

        result = driver.find_element(By.ID, "password").text
        result = result.replace("Пароль: ", "")

        return result

    def run(self):
        with self.driver as driver:
            data = self.get_result(driver, self.url)

            print(data)


def main():
    d = DataDriver()
    d.run()


main()
