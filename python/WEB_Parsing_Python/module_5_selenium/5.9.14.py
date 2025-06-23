# Инициализация: Запустите браузер через Selenium и загрузите страницу.
# Настройка размеров: Откройте окно браузера так, чтобы рабочая (видимая) область страницы точно соответствовала 555x555 пикселям. Не забудьте учесть размеры рамок и панелей браузера при расчете!
# Анализ: Когда условие будет выполнено секретный ключ появится в id="result";
# Действие: Извлеките содержимое данного элемента и вставьте в поле для ответа.
# Подсказка: Убедитесь, что учли все элементы интерфейса браузера при настройке размера окна. Размеры рамок и панелей могут влиять на видимую область, и их необходимо учитывать в вашем решении.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/window_size/1/"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)
        self.action = ActionChains(self.driver)
        self.default_size = 555

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

        def_width = driver.get_window_size()["width"]
        def_height = driver.get_window_size()["height"]

        work_width = driver.execute_script("return window.innerWidth;")
        work_height = driver.execute_script("return window.innerHeight;")

        diff_width = def_width - work_width
        diff_height = def_height - work_height

        driver.set_window_size(
            self.default_size + diff_width, self.default_size + diff_height
        )

        result = driver.find_element(By.ID, "result").text
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
