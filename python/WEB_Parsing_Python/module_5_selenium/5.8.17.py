# Инициализация: Используя Selenium, откройте заданный веб-сайт.
#
# Скроллинг: На сайте имеется список из 100 элементов, который расширяется при скроллинге (infinity scroll).
#
# Сбор данных: Кликайте или скролльте по интерактивным элементам, чтобы раскрыть все 100 элементов списка. Используйте Keys.DOWN или методы ActionChains(driver).
#
# Агрегация: Извлеките все числовые значения из этих элементов и сложите их.
#
# Отправка ответа: Вставьте собранную сумму чисел в предназначенное поле на сайте.
#
#
#
# Подсказки и заметки
# Помните о задержках при загрузке элементов.
#
# Последний элемент списка имеет класс last-of-list. Используйте это для прерывания цикла скроллинга.
#
# Внимательно изучите структуру HTML-страницы. Это поможет вам понять, как искать нужные элементы.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/infiniti_scroll_1/"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)
        self.action = ActionChains(self.driver)
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

        while True:
            last_child = driver.find_element(
                By.CSS_SELECTOR, ".scroll-container>span:last-child"
            )

            if last_child.get_attribute("class") == "last-of-list":
                break

            self.action.move_to_element(last_child).scroll_by_amount(0, 5000).perform()

        span = driver.find_elements(By.TAG_NAME, "span")

        result = 0

        for s in span:
            self.action.move_to_element(s).perform()
            s.find_element(By.TAG_NAME, "input").click()

            result += int(s.text)

            if s.get_attribute("class") == "last-of-list":
                break

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
