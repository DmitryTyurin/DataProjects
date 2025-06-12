# Прибытие на "Остров": Используйте Selenium для открытия заданного веб-сайта.
# Охота на сокровище: В элементе с id="result" иногда появляется число — это и есть ваше сокровище. Проблема в том, что оно появляется очень редко. Вам придется обновлять страницу множество раз, пока не увидите это число.
# Клад в руках: Как только число появится, скопируйте его и вставьте в предназначенное для этого поле ответа на вашем курсе.


from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/methods/1/index.html"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)

    @staticmethod
    def setup_options():
        from selenium.webdriver.chrome.options import Options

        options = Options()
        options.add_argument("--headless")  # Без графического интерфейса
        # options.add_argument('--disable-gpu')  # Отключаем GPU
        # options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна

        return options

    @staticmethod
    def get_result(driver, url):
        driver.get(url)

        while True:
            result = driver.find_element(By.ID, "result").text
            driver.refresh()

            if result.isdigit():
                return result

    def run(self):
        with self.driver as driver:
            data = self.get_result(driver, self.url)

            print(data)


def main():
    d = DataDriver()
    d.run()


main()
