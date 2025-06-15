# Запустите ваш кибер-копатель и отправьтесь на заданный сайт.
# Особая задача сбора: Соберите только те "печеньки", значения которых имеют чётные числа после символа "_". Например, если cookie имеет имя "session_12", число "12" является чётным, и это именно то, что вам нужно.
# Анализ и суммирование: Суммируйте числовые значения этих особых "печенек". Это сумма будет вашим ключом.
# Ввод ответа: После расшифровки вставьте ваш ключ в специальное поле для ответов на степик. Успех здесь означает ваш переход на следующий уровень задания.

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
        # options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна

        return options

    def get_result(self, driver, url):
        import time

        driver.get(url)

        cookies = driver.get_cookies()

        for cookie in cookies:
            name = cookie.get("name")
            name_last_char = int(name[-1])
            value = cookie.get("value")

            if name_last_char % 2 == 0:
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
