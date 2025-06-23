# 1️⃣ С помощью Selenium запустите браузер и откройте главную страницу сайта-тренажера
# 2️⃣ На главной странице соберите 5 ссылок и откройте их в новых вкладках.
# 🟢Примечание: Главная страница доступна даже без Selenium, но для остальных страниц требуется управление через Selenium!
#
# 3️⃣ Спустя 3 сек, на каждой странице появится по 3 числа, соберите их и получите сумму всех чисел.
# 4️⃣ Вернитесь на главную страницу и вставьте полученное значение в поле и нажмите кнопку "Проверить"
# 5️⃣ Если вы все сделали правильно, система выдаст пароль. Считайте его и введите на степик в поле ниже между кавычками.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/8/8.1.2/index.html"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)
        self.action = ActionChains(self.driver)
        self.all_numbers = []

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

        links = driver.find_elements(By.TAG_NAME, "a")
        links = [link.get_attribute("href") for link in links]

        for link in links:
            driver.switch_to.new_window("tab")
            driver.get(link)
            time.sleep(4)
            result = driver.find_element(By.CSS_SELECTOR, "#codePlaceholder").text

            self.all_numbers.append(result)

        total_sum = self.get_sum()

        driver.switch_to.window(driver.window_handles[0])
        driver.find_element(By.ID, "sumInput").send_keys(total_sum)
        driver.find_element(By.ID, "checkButton").click()

        result = driver.find_element(By.ID, "passwordDisplay").text
        result = result.split(":")[-1].strip()

        return result

    def get_sum(self):
        total_sum = 0

        for string in self.all_numbers:
            numbers = string.split("\n")
            for num in numbers:
                total_sum += int(num)

        return total_sum

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
