# Начало путешествия: Войдите на указанный сайт с помощью Selenium, где четыре пронумерованных блока ужe ждут
# своего героя - красного квадрата.
# Миссия перемещения: Ваша задача - написать скрипт, который возьмёт на себя роль проводника и поможет красному
# квадрату посетить каждый из этих блоков, перетаскивая его поочерёдно в каждый из них.
# Токен победы: Как только красный квадрат посетит все блоки, на сцене появится токен - символ вашего успеха и
# завершения миссии. Этот токен необходимо будет вставить в поле для ответа, чтобы закрепить ваш успех и
# завершить задание.
# Значение путешествия: Получив токен, вы не просто завершите задачу. Вы докажете себе и миру, что способны направлять
# и поддерживать, что у вас есть терпение и внимательность, чтобы помочь даже маленькому
# красному квадрату найти своё место в этом мире.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://parsinger.ru/draganddrop/2/index.html"


# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)

        draggable_element = driver.find_element(By.ID, "draggable")
        box_elements = driver.find_elements(By.CLASS_NAME, "box")

        for box in box_elements:
            actions.drag_and_drop(draggable_element, box).perform()

        result = wait.until(EC.element_to_be_clickable((By.ID, "message"))).text

        if result:
            print(result)


get_result(URL)
