# 1️⃣ Зайдите на сайт-тренажёр с помощью Selenium.
# 2️⃣ Перетащите мистера Гриффина в бассейн и получите пароль в виде фразы.
# 3️⃣ Извлеките текст пароля из появившегося элемента с id="password" и вставьте его в поле ниже между кавычками.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/7/7.3.1/index.html"
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

        source = driver.find_element(By.ID, "draggable")
        target = driver.find_element(By.ID, "target")

        (
            self.action
            .drag_and_drop(source, target)
            .perform()
        )

        result = driver.find_element(By.ID, "password").text
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
