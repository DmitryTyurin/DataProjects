# 1️⃣ Зайдите на сайт-тренажёр с помощью Selenium.
# 2️⃣ Установите cookie с именем "secretKey" и значением "selenium123".
# 3️⃣ Обновите страницу. Если всё сделано правильно, появится пароль в элементе с id="password".
# 4️⃣ Извлеките пароль .text
# 5️⃣ Вставьте пароль в поле ниже, между кавычками.


from selenium import webdriver
from selenium.webdriver.common.by import By


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/6/6.3.3/index.html"
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

        driver.add_cookie({"name": "secretKey", "value": "selenium123"})
        time.sleep(3)

        driver.refresh()

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
