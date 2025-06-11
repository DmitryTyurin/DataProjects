# 🔹 Задача: используя каскадный поиск найдите элемент на странице, кликните на него, и считайте появившийся атрибут в теге.
# 1️⃣ Зайти на сайт-тренажер с помощью Selenium.
# 2️⃣ Найти родительский элемент с идентификатором parent_id.
# 3️⃣ Внутри этого родительского элемента найти первый дочерний элемент с классом child_class и кликнуть его.
# 4️⃣ После клика в этом теге появится атрибут password, считать значение этого атрибута с помощью .get_attribute(), это и будет пароль.
# 5️⃣ Вставить полученный пароль в поле ниже между кавычек.


from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/3/3.3.1/index.html"
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
    def get_result(driver, url):
        driver.get(url)

        elements = driver.find_element(By.ID, "parent_id")
        child = elements.find_element(By.CLASS_NAME, "child_class")
        child.click()
        result = child.get_attribute("password")

        return result

    def run(self):
        with self.driver as driver:
            data = self.get_result(driver, self.url)

            print(data)


def main():
    d = DataDriver()
    d.run()


main()
