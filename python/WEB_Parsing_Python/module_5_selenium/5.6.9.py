# Исследование территории: Откройте веб-сайт с помощью Selenium. Проанализируйте поля, с которыми предстоит работать.
# Миссия "Синхронизация": На странице находятся 100 текстовых полей: 50 серых и 50 синих. Ваша задача — перенести числа из серых полей в синие.
# Проверка и контроль: Нажмите на кнопку "Проверить". Если перенос чисел прошёл успешно, поля станут зелёными.
# Получение кода: Секретный код появится только в том случае, если все поля успешно стали зелёными. Секретный код нужно будет вставить в поле для ответа на степик.
# ​​Код должен появится ниже большой зеленой кнопки!

from selenium import webdriver
from selenium.webdriver.common.by import By


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/5.5/4/1.html"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)

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

        elements = driver.find_elements(By.CLASS_NAME, "parent")

        for element in elements:

            color = element.find_elements(By.TAG_NAME, "textarea")
            nums = 0

            for item in color:
                if item.get_attribute("color") == "gray":
                    nums = item.text
                    item.clear()

                if item.get_attribute("color") == "blue":
                    item.send_keys(nums)

            element.find_element(By.TAG_NAME, "button").click()

        driver.find_element(By.ID, "checkAll").click()

        result = driver.find_element(By.ID, "congrats").text

        return result

    def run(self):
        with self.driver as driver:
            data = self.get_result(driver, self.url)

            print(data)


def main():
    d = DataDriver()
    d.run()


main()
