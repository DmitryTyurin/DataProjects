# Инициализация: Используя Selenium, откройте заданный сайт.
# Анализ списков размеров: У вас есть два списка размеров – window_size_x и window_size_y.
# Тестирование: Примените каждое сочетание размеров из этих списков к окну вашего браузера.
# Поиск результата: После каждой установки размера проверяйте содержимое элемента с идентификатором id="result" на странице.
# Извлечение данных: Как только найдете уникальное сочетание, при котором на странице появляется число, скопируйте его и вставьте в поле для ответа.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/window_size/2/index.html"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)
        self.action = ActionChains(self.driver)
        self.window_size_x = [
            616,
            648,
            680,
            701,
            730,
            750,
            805,
            820,
            855,
            890,
            955,
            1000,
        ]
        self.window_size_y = [
            300,
            330,
            340,
            388,
            400,
            421,
            474,
            505,
            557,
            600,
            653,
            1000,
        ]

    @staticmethod
    def setup_options():
        from selenium.webdriver.chrome.options import Options

        options = Options()
        options.add_argument("--headless")  # Без графического интерфейса
        options.add_argument("--disable-gpu")  # Отключаем GPU
        # options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна

        return options

    def get_result(self, driver, url):
        import time

        driver.get(url)

        def_width = driver.get_window_size()["width"]
        def_height = driver.get_window_size()["height"]

        work_width = driver.execute_script("return window.innerWidth;")
        work_height = driver.execute_script("return window.innerHeight;")
        print(f"Размер окна по умолчанию: {def_width}, {def_height}")

        diff_width = def_width - work_width
        diff_height = def_height - work_height
        print(f"Разница размеров окна: {diff_width}, {diff_height}")

        for x in self.window_size_x:
            for y in self.window_size_y:
                print(x, y)
                driver.set_window_size(x + diff_width, y + diff_height)
                result = driver.find_element(By.ID, "result").text

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
