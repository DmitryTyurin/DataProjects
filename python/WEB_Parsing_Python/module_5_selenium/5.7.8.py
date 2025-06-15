# Этапы миссии:
# Вооружитесь браузером и пусть ваш код проникнет на сайт.
# Поиск секретных cookies: Найдите все скрытые secret_cookie_, которые могут содержать важную информацию.
# Дешифровка и анализ: Суммируйте числовые значения всех secret_cookie_. Это может быть частью шифра или ключом к следующему уровню.
# Ввод ответа: Вставьте полученную сумму в поле ответа степик. Это ваш ключ к успешному завершению миссии.

from selenium import webdriver
from selenium.webdriver.common.by import By


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/methods/3/index.html"
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

    def get_result(self, driver, url):
        import time

        driver.get(url)

        cookies = driver.get_cookies()

        for cookie in cookies:
            name = cookie.get("name")
            value = cookie.get("value")

            if name.startswith("secret_cookie"):
                self.result.append(int(value))

        return self.result

    def run(self):
        with self.driver as driver:
            data = self.get_result(driver, self.url)

            print(sum(self.result))


def main():
    import time

    start_time = time.perf_counter()

    d = DataDriver()
    d.run()

    end_time = time.perf_counter()

    print(f"Время выполнения: {end_time - start_time:.2f} секунд")


main()
