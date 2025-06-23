# Загадочный Замок: Начните свою экспедицию, открыв сайт с помощью Selenium.
# Таинственные Блоки: Блоки с появляются благодаря магии атрибута display.
# Ваш щит и меч в этом бою – метод EC.visibility_of(element) или EC.visibility_of_element_located(locator)
# Карта Ключей: С вами список ID ids_to_find.
# Эти ID – не просто случайные символы, это карта к древнему коду,
# вам необходимо дождаться появления и кликнуть по блокам именно с этими ID.
# Испытание Ловкости: Но будьте внимательны!
# Каждый клик вне списка ids_to_find обнуляет ваши успехи, и вам придется начать все сначала.
# Так что меряйте семь раз, прежде чем кликнуть!
# Испытание Терпения: Остерегайтесь ловушек!
# Каждый элемент на вашем пути может появиться в самый неожиданный момент.
# Ваша задача – быть настороже и дождаться момента, когда ключевые элементы покажут себя.
# Секретный Код: Если вы правильно активируете все нужные порталы, перед вами раскроется алерт с древним кодом.
# Этот код – залог вашего успеха в решении задачи.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://parsinger.ru/selenium/5.9/3/index.html"

ids_to_find = [
    "xhkVEkgm",
    "QCg2vOX7",
    "8KvuO5ja",
    "CFoCZ3Ze",
    "8CiPCnNB",
    "XuEMunrz",
    "vmlzQ3gH",
    "axhUiw2I",
    "jolHZqD1",
    "ZM6Ms3tw",
    "25a2X14r",
    "aOSMX9tb",
    "YySk7Ze3",
    "QQK13iyY",
    "j7kD7uIR",
]

# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        for i in ids_to_find:
            elem_loc = (By.ID, i)

            wait = WebDriverWait(driver, 120, poll_frequency=0.1)
            wait.until(EC.visibility_of_element_located(elem_loc)).click()

        print(driver.switch_to.alert.text)


get_result(URL)
