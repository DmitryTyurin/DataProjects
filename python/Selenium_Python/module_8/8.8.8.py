# Вход в Мир Таинства: Используйте Selenium для открытия указанного сайта и подготовьтесь к встрече с чек боксом,
# обладающим свойствами непредсказуемости.
# Погоня за Мгновением: Чек бокс, который вы встретите, обладает уникальной способностью внезапно появляться и исчезать.
# Он не любит, когда его ловят на месте, и потому ваша задача - быть настолько внимательным и быстрым,
# чтобы ухватить его в момент активации.
# Методы Ожидания: Вооружитесь методами ожидания Selenium,
# ибо только они помогут вам в этой неравной битве со временем и неопределенностью.
# Дождитесь момента, когда чек бокс активируется, и в тот же миг нажмите на кнопку "Проверить".
# Доказательство Мастерства: Если вы справитесь с задачей, и проверка пройдет успешно,
# вы получите секретный код. Код, который станет вашим трофеем и доказательством того, что даже
# в мире неопределенности вы можете найти уверенность и решимость.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

URL = "https://parsinger.ru/selenium/5.9/6/index.html"


# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_located_to_be_selected((By.ID, "myCheckbox")))

        driver.find_element(By.TAG_NAME, "button").click()

        result = driver.find_element(By.ID, "result").text

        if result:
            print(result)


get_result(URL)
