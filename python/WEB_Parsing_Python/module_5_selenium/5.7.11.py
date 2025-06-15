# Переход на сайт: Используйте Selenium для того, чтобы перейти на целевой веб-сайт.
#
# # Удаление всех кукис для чистого эксперимента
# driver.delete_all_cookies()
# Загрузка данных: Загрузите 100 комплектов cookies (под спойлером внизу степа), присланных хакерской группой. Каждый cookie принадлежит одному из хакеров противоборствующей группы.
#
# # Пример добавления кукис
# driver.add_cookie({'name': 'cookie_name', 'value': 'cookie_value'})
# Обновление страницы: Используйте driver.refresh() для того, чтобы применить новые cookies.
# # Обновление страницы
# driver.refresh()
# Анализ и Вербовка: Пройдитесь по всем кукам и определите самого молодого и перспективного хакера — того, кто младше всех и знает больше всего языков программирования.
# Извлечение данных: После того, как вы определите, кто из хакеров наиболее перспективен, извлеките "value" из его cookie.
# cookies = driver.get_cookies()
# for cookie in cookies:
#     print(cookie['name']) # или cookie['value'] чтобы получить их значение
# Завершающий этап: Вставьте полученное значение cookie['value'] в поле для ответов на Степике.
# Подсказки и трюки:
#
# Используйте все доступные вам методы и функции для анализа cookies.
# Внимательно изучите каждый cookie. Иногда самая ценная информация скрыта в самых неочевидных местах.

from selenium import webdriver
from selenium.webdriver.common.by import By


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/5.6/1/index.html"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)
        self.temp_age_lang = {"name": "", "age": 99, "count_lang": 0}

    @staticmethod
    def setup_options():
        from selenium.webdriver.chrome.options import Options

        options = Options()
        # options.add_argument("--headless")  # Без графического интерфейса
        # options.add_argument('--disable-gpu')  # Отключаем GPU
        options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна

        return options

    def get_result(self, driver, url):
        import datetime
        import time

        driver.get(url)

        driver.delete_all_cookies()

        for cookie in self.cookies:
            driver.add_cookie(cookie)

            driver.refresh()

            name = driver.find_element(By.XPATH, '//span[@id="name"]').text[6:]
            age = int(driver.find_element(By.XPATH, '//span[@id="age"]').text[5:])
            count_lang = len(
                driver.find_element(By.XPATH, '//ul[@id="skillsList"]').text.split()
            )
            if (
                age < self.temp_age_lang["age"]
                and count_lang > self.temp_age_lang["count_lang"]
            ):
                self.temp_age_lang["name"] = name
                self.temp_age_lang["age"] = age
                self.temp_age_lang["count_lang"] = count_lang
                self.temp_age_lang["cookie_value"] = cookie["value"]

    def run(self):
        with self.driver as driver:
            self.get_result(driver, self.url)

            print(self.temp_age_lang)


def main():
    import time

    start_time = time.perf_counter()

    d = DataDriver()
    d.run()

    end_time = time.perf_counter()

    print(f"Время выполнения: {end_time - start_time:.2f} секунд")


main()
