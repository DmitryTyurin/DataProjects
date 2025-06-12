# Откройте указанный сайт с помощью Selenium. Здесь вас встретят 100 текстовых полей, и рядом с некоторыми из них будут чекбоксы. Главная загвоздка: чекбоксы и их состояние ("checked" или "unchecked") определяются случайным образом.
# Пройдитесь по всем текстовым полям и соберите числа только из тех, которые имеют рядом активные чекбоксы.
# Особенности и условности
# Поля и чекбоксы могут загружаться в разных комбинациях, поэтому рассчитывать на конкретную последовательность или паттерн не стоит.
# Чекбоксы могут быть в двух состояниях: checked (отмечены) и unchecked (не отмечены). Мы интересуемся только числами из полей с отмеченными чекбоксами.
# Собранные числа необходимо суммировать и полученный результат вставить в поле ответа степик.

from selenium import webdriver
from selenium.webdriver.common.by import By


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/5.5/3/1.html"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)
        self.result = 0

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

        elements = driver.find_elements(By.CLASS_NAME, "parent")

        for element in elements:
            checkbox = element.find_element(By.CLASS_NAME, "checkbox")

            if checkbox.is_selected():
                self.result += int(element.find_element(By.TAG_NAME, "textarea").text)

        return self.result

    def run(self):
        with self.driver as driver:
            data = self.get_result(driver, self.url)

            print(data)


def main():
    d = DataDriver()
    d.run()


main()
