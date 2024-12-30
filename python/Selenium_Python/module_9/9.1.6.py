# Вход в виртуальный мир: Откройте указанный сайт с помощью Selenium, и погрузитесь в мир,
# где ваши действия определяют исход событий.
# Задача перемещения: На сайте вас встретят два поля. В одном из них - красный блок, который ждет вашей помощи,
# чтобы пересечь границы и оказаться во втором поле. Используйте Selenium для написания скрипта,
# который аккуратно перетащит красный блок из первого поля во второе.
# Появление токена: Как только блок достигнет своей цели, на сцене появится токен - символ вашего успеха
# и умения справляться с задачами.
# Ваша следующая миссия - взять этот токен и вставить его в поле для ответа, чтобы закрепить свою победу.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://parsinger.ru/draganddrop/1/index.html"


# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        from_ = driver.find_element(By.ID, "field1")
        to_ = driver.find_element(By.ID, "field2")

        actions = ActionChains(driver)
        actions.drag_and_drop(from_, to_).perform()

        result = driver.find_element(By.ID, "result").text

        if result:
            print(result)


get_result(URL)
