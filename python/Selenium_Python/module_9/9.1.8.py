# Встреча с зелёными квадратами: При открытии сайта вы увидите 10 зелёных квадратов, каждый из которых готов к переезду.
# Ваша задача - помочь им в этом.
# Путешествие к серой области: Перетаскивайте квадраты один за другим в серую область.
# Обратите внимание, каждый квадрат несет в себе частицу целого, и только объединив их в серой области,
# вы сможете увидеть полную картину.
# Получение секретного кода:
# Как только последний зелёный квадрат окажется в серой области, перед вами откроется секретный код.
# Этот код символизирует успешное завершение задачи и ваше понимание важности каждого шага в путешествии


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://parsinger.ru/selenium/5.10/2/index.html"


# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        end = driver.find_element(By.CLASS_NAME, "draganddrop_end")
        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)

        for elem in range(1, 11):
            start = driver.find_element(By.ID, f"draganddrop{elem}")
            actions.drag_and_drop(start, end).perform()

        result = wait.until(EC.element_to_be_clickable((By.ID, "message"))).text

        if result:
            print(result)


get_result(URL)
