# 1️⃣ Зайдите на сайт-тренажёр с помощью Selenium.
# 2️⃣ Найдите все элементы с тегом <a>.
# 3️⃣ Пройдитесь по каждому элементу <a> и проверьте значение атрибута stormtrooper. Суммируйте все числовые значения атрибута stormtrooper для получения общего количества штурмовиков.
# 4️⃣ Вставьте полученное значение всех штурмовиков на странице тренажера и нажмите кнопку "Проверить"  , появится заветный пароль(в виде фразы), считайте его с помощью .text.
# 5️⃣ Вставьте пароль в поле ниже, между кавычками на Stepik.
# 💡 Совет: заведите переменную (счетчик) для подсчёта общего количества штурмовиков в армии.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/3/3.3.3/index.html"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)
        self.result = []

    @staticmethod
    def setup_options():
        from selenium.webdriver.chrome.options import Options

        options = Options()
        # options.add_argument("--headless")  # Без графического интерфейса
        # options.add_argument('--disable-gpu')  # Отключаем GPU
        options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна

        return options

    @staticmethod
    def extract_digits(text):
        import re

        pattern = r"\d{1,}\.\d{1,}|\d{1,}"
        digits = "".join(re.findall(pattern, text))

        if digits == "":
            return 0
        else:
            return int(digits)

    def get_result(self, driver, url):
        driver.get(url)

        elements = driver.find_elements(By.TAG_NAME, "a")

        for element in elements:
            attr = self.extract_digits(element.get_attribute("stormtrooper"))
            self.result.append(attr)

        sum_result = sum(self.result)

        driver.find_element(By.ID, "inputNumber").send_keys(sum_result)
        driver.find_element(By.ID, "checkBtn").click()

        result = driver.find_element(By.ID, "feedbackMessage").text
        result = result.split(":")[1].strip()

        return result

    def run(self):
        with self.driver as driver:
            data = self.get_result(driver, self.url)

            print(data)


def main():
    d = DataDriver()
    d.run()


main()
