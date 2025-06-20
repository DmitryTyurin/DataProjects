# Инициализация: Откройте заданный веб-сайт с помощью Selenium.
#
# Обнаружение чекбоксов: На сайте будет 100 чекбоксов. Если кликнуть на чекбокс, может появится число в теге span
#
# ​​​​​​​<span id="result1">954</span>
#
#
# Вычисление: Соберите все эти числа и сложите их.
#
# Отправка ответа: Введите сумму всех чисел, в поле ответа на Stepik.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/scroll/2/index.html"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)
        self.action = ActionChains(self.driver)
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
        import time

        driver.get(url)

        for i in range(1, 101):
            element = driver.find_element(By.ID, f"{i}")
            ActionChains(driver).send_keys(Keys.TAB).click(element).perform()
            time.sleep(0.1)
            result = driver.find_element(By.ID, f"result{i}").text

            if result != "":
                self.result.append(int(result))

        return sum(self.result)

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
