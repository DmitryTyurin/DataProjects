# 1️⃣ Зайти на сайт-тренажёр с помощью Selenium.
# 2️⃣ Получить список всех cookies.
# 3️⃣ Найти название песни.
# 4️⃣ Вставить название в поле для проверки и нажать кнопку «Проверить».
# 5️⃣ Извлечь девиз одного известного персонажа из Dota 2из элемента с id="result"
# 6️⃣ Вставить девиз в поле ниже, между кавычками.

from selenium import webdriver
from selenium.webdriver.common.by import By


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/6/6.3/index.html"
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

        driver.get(url)

        cookie = driver.get_cookies()
        name_cookie = cookie[0].get("name")

        driver.find_element(By.ID, "phraseInput").send_keys(name_cookie)
        driver.find_element(By.ID, "checkButton").click()

        result = driver.find_element(By.ID, "result").text

        return result

    def run(self):
        with self.driver as driver:
            data = self.get_result(driver, self.url)

            print(data)


def main():
    d = DataDriver()
    d.run()


main()
