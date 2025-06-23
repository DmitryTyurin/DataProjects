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
