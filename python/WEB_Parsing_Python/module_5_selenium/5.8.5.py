# Идентификация элемента: Первым делом необходимо найти элемент, с которым вы хотите взаимодействовать.
# # Пример поиска элемента по ID
# browser.find_element(By.ID, 'btn')
# Получение фокуса: Воспользуйтесь методом scrollIntoView для того, чтобы прокрутить страницу так, чтобы нужный элемент оказался в видимой области.
# # Пример получения фокуса элемента
# element = browser.find_element(By.CLASS_NAME, 'btn')
# browser.execute_script("return arguments[0].scrollIntoView(true);", element)
# Клик по элементу: Теперь, когда элемент в фокусе, попробуйте снова выполнить клик.
# Проверка результата: Убедитесь, что ваше взаимодействие с элементом привело к желаемому результату(в теге с  <p id="result">788544</p> появляется уникальное для каждой кнопки число).
# Суммирование:  Суммируйте все полученные числа.
# Завершающий этап: Вставьте полученную сумму в поле ответов на Степике.


from selenium import webdriver
from selenium.webdriver.common.by import By


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/scroll/4/index.html"
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

        element = driver.find_elements(By.CLASS_NAME, "btn")

        for element in element:
            driver.execute_script("arguments[0].scrollIntoView();", element)
            element.click()

            result = driver.find_element(By.ID, "result").text
            self.result.append(int(result))

        return self.result

    def run(self):
        with self.driver as driver:
            data = self.get_result(driver, self.url)

            print(sum(data))


def main():
    import time

    start_time = time.perf_counter()

    d = DataDriver()
    d.run()

    end_time = time.perf_counter()

    print(f"Время выполнения: {end_time - start_time:.2f} секунд")


main()
