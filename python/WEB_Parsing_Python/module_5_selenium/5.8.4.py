# 🔹 Задача: На сайте-тренажёре вам предстоит выполнить несколько шагов, связанных с прокруткой и взаимодействием с элементами.
#
# 1️⃣ Откройте сайт-тренажёр с помощью Selenium.
# 2️⃣ Прокрутите страницу вниз до кнопки "Финиш!". Используйте scrollIntoView()метод прокрутки к элементу с id="target".
# 3️⃣ Нажмите на кнопку "Финиш!".
# 4️⃣ Извлеките секретный ключ.
# 5️⃣ Вставьте пароль в поле ниже, между кавычками.
# 💡 Совет: выведите результат в print().


from selenium import webdriver
from selenium.webdriver.common.by import By


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/6/6.5/index.html"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)

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

        target = driver.find_element(By.ID, "target")
        driver.execute_script("arguments[0].scrollIntoView();", target)
        target.click()

        result = driver.find_element(By.ID, "secret-key").text
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
