# 1️⃣ Перейдите на сайт-тренажёр с помощью Selenium.
# 2️⃣ Используя метод key_down(), создайте цепочку событий, которая имитирует зажатие клавиш CTRL + ALT + SHIFT + T.
# 3️⃣ Используя key_up() в той же цепочке событий, отожмите клавиши CTRL + ALT + SHIFT+T
# 4️⃣ Извлеките пароль из появившегося элемента с атрибутом key="access_code" и вставьте его в поле ниже между кавычками.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/7/7.3.3/index.html"
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

        (
            self.action.key_down(Keys.CONTROL)
            .key_down(Keys.ALT)
            .key_down(Keys.SHIFT)
            .key_down("T")
            .perform()
        )

        time.sleep(1)

        (
            self.action.key_up(Keys.CONTROL)
            .key_up(Keys.ALT)
            .key_up(Keys.SHIFT)
            .key_up("T")
            .perform()
        )

        result = driver.find_element(
            By.CSS_SELECTOR, "#passwordContainer > p > span"
        ).text
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
