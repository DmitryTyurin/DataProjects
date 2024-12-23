# Стартовая Позиция: Запустите Selenium и откройте данный веб-сайт.
# Убедитесь, что ваша станция готова к операции.
# Сбор Урана: Пройдитесь по каждому кусочку урана на странице и кликните по нему.
# Это поможет нам вернуть его обратно на корабль.
# Получение Секретного Кода: Как только в открытом космосе не останется ни одного кусочка урана,
# команда пришлёт вам в alert-окне секретный код.
# Финальный Этап: Вставьте полученный секретный код в необходимое поле для завершения операции.
# Подсказки и заметки:
# Будьте быстрыми и точными. Космос не будет ждать!
# Используйте уже знакомые методы поиска элементов в Selenium, чтобы точно найти все кусочки урана.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://parsinger.ru/selenium/5.7/1/index.html"

# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        elements = driver.find_elements(By.CLASS_NAME, "button-container")

        for element in elements:
            element.click()

        alert = driver.switch_to.alert.text

        print(alert)


get_result(URL)
