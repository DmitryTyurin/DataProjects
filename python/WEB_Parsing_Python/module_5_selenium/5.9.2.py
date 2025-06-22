# 1️⃣ С помощью Selenium зайдите на сайт-тренажер.
# 2️⃣ На главной странице находятся три кнопки, каждая из которых вызывает модальное окно.
# 3️⃣ Выполните следующие действия:
# Для окна Alert – кликните по кнопке и вызовите метод accept(), чтобы закрыть окно.
# Для окна Prompt – кликните по соответствующей кнопке, введите точный текст «Alert»(не текст из окна Alert, а просто слово Alert) через .send_keys() , затем подтвердите ввод методом .accept()
# Для окна Confirm – кликните по кнопке и нажмите ОК
# 4️⃣ Если все модальные окна обработаны правильно, на странице динамически отобразится секретный пароль.
# 5️⃣ Считайте пароль из DOM и вставьте его в поле ниже на платформе Stepik.
# 🟢 Внимание: Пароль отобразится только при использовании Selenium для автоматизации взаимодействия с модальными окнами.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/8/8.3.1/index.html"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)
        self.action = ActionChains(self.driver)
        self.button_list = ["alertButton", "promptButton", "confirmButton"]

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

        for button in self.button_list:
            if button == "alertButton":
                driver.find_element(By.ID, button).click()
                time.sleep(1)
                driver.switch_to.alert.accept()
            if button == "promptButton":
                driver.find_element(By.ID, button).click()
                time.sleep(1)
                driver.switch_to.alert.send_keys("Alert")
                time.sleep(1)
                driver.switch_to.alert.accept()
            if button == "confirmButton":
                driver.find_element(By.ID, button).click()
                time.sleep(1)
                driver.switch_to.alert.accept()
        time.sleep(2)

        result = driver.find_element(By.ID, "secretKey").text
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
