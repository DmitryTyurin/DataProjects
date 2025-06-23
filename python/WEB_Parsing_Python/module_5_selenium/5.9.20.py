# Погружение: Откройте сайт с помощью Selenium.
# Активация тайных порталов: Нажимая на каждую из 10 кнопок, вы активируете ворота в другую вкладку. Это ваш шанс найти одну из частей кода.
# Исследование: В каждой новой вкладке ищите в title число — ваш ключ к решению.
# Сбор информации: Соберите все 10 чисел и сложите их.
# Завершение миссии: Вставьте итоговую сумму в поле для ответа на исходной странице.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://parsinger.ru/blank/3/index.html"

# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        elements = driver.find_elements(By.CLASS_NAME, "buttons")

        result = 0

        for element in elements:
            element.click()

        for x in range(len(driver.window_handles)):
            driver.switch_to.window(driver.window_handles[x])

            num = driver.execute_script("return document.title;")

            result += int(num) if num.isdigit() else 0

        print(result)


get_result(URL)
