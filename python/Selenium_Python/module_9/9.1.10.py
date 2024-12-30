# Встреча с цветными блоками: Посетите указанный сайт и вы увидите множество цветных блоков,
# каждый из которых ждет своего момента, чтобы встретить свою пару.
# Танец пар: Ваша задача - написать скрипт на Selenium, который поможет каждому блоку найти
# и соединиться со своей парой.
# Пара определяется по цвету блока, и именно цвет будет вашим проводником в этом танце.
# Сообщение победы: Как только все пары найдены и соединены, на экране появится сообщение.
# Это сообщение не просто говорит о том, что задача выполнена, оно несет в себе глубинный смысл
# и радость от успешно завершенного путешествия.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains


URL = "https://parsinger.ru/selenium/5.10/3/index.html"


# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)

        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "draganddrop")))

        elements = driver.find_elements(By.CLASS_NAME, "draganddrop")
        targets = driver.find_elements(By.CLASS_NAME, "draganddrop_end")

        for element, target in zip(elements, targets):
            actions.click_and_hold(element).perform()
            actions.drag_and_drop(element, target).perform()

        result = wait.until(EC.element_to_be_clickable((By.ID, "message"))).text

        if result:
            print(result)


get_result(URL)
