# Запуск: Откройте основной сайт с помощью Selenium. С этой точки начнётся ваша экспедиция в поисках "Бессмертного Печенюшка".
# Следование за линками: На основной странице будет 42 ссылки. Открывайте каждую из них, чтобы исследовать и выяснить, какой из cookies имеет самый долгий срок жизни.
# Вычисление жизнеспособности: Для каждой открытой страницы анализируйте срок жизни её cookie ['expiry']. Сохраняйте эти данные для последующего сравнения.
# Коронация Бессмертного: После проверки всех 42 страниц определите, на какой из них находится cookie с самым долгим сроком жизни. С этой страницы извлеките число которое лежит в  теге <p id="result">INT</p>.
# Завершающий этап: Вставьте полученное число в специальное поле для степик. Поздравляем, вы нашли "Бессмертного Печенюшка" и преуспели в этой миссии!

from selenium import webdriver
from selenium.webdriver.common.by import By


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/methods/5/index.html"
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
        import datetime
        import time

        driver.get(url)
        links = driver.find_elements(By.TAG_NAME, "a")

        for link in links:
            link_url = link.get_attribute("href")
            link.click()

            cookies = driver.get_cookies()

            expiry = []
            for cookie in cookies:
                expiry_date = datetime.datetime.fromtimestamp(cookie["expiry"])
                expiry.append(expiry_date)

            max_expiry = max(expiry)

            self.result.append((max_expiry, link_url))
            driver.back()

        max_entry = max(self.result, key=lambda x: x[0])[1]

        driver.get(max_entry)
        result = int(driver.find_element(By.ID, "result").text)

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
