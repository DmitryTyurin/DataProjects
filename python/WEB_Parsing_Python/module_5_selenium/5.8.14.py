# 1️⃣ Перейдите на сайт-тренажёр с помощью Selenium.
# 2️⃣Под каждым контейнером находится статусный блок, который изначально показывает «Статус: не прокручено». С помощью ActionChains используя метод отправки клавиши END, прокрутить содержимое каждого контейнера до самого низа. Как только содержимое контейнера прокручено до конца, соответствующий статусный блок должен обновиться: текст изменится на «Прокручено!», а фон изменится на зелёный (подсветка).
# 3️⃣После того как оба контейнера прокручены до конца, ниже появляется блок с секретным паролем. Извлеките пароль из элемента, где он отображается (элемент имеет атрибут key="access_code").
# 4️⃣ Вставьте пароль здесь в поле ниже.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/7/7.3.5/index.html"
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

        containers = driver.find_elements(By.CLASS_NAME, "scroll-container")

        for container in containers:
            ActionChains(driver).click(container).send_keys(Keys.END).perform()

        time.sleep(1)

        result = driver.find_element(By.CSS_SELECTOR, '[key="access_code"]').text
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
