# Вход на сайт: Откройте загадочный сайт с помощью Selenium.
# Ожидание: На сайте есть кнопка, но она не активна сразу.
# Она "пробуждается" в случайный момент времени, в течение 1-3 секунд после загрузки.
# Быстрый рефлекс: После нажатия на эту кнопку, начните наблюдение за заголовком страницы (title).
# Он будет меняться, и вам нужно действовать стремительно!
# Момент правды: Когда заголовок страницы станет "345FDG3245SFD", быстро извлеките код из элемента с id="result".
# Финиш: Завершите задачу, вставив полученный код в поле для ответа.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://parsinger.ru/expectations/3/index.html"
TITLE = "345FDG3245SFD"

# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "btn"))
        ).click()
        WebDriverWait(driver, 30).until(EC.title_is(TITLE))

        result = driver.find_element(By.ID, "result").text

        if result:
            print(result)
        else:
            pass


get_result(URL)
