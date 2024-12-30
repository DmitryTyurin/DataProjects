# Открытие мира: Используйте Selenium для того, чтобы открыть сайт.
# Миссия броска: В вашем распоряжении 8 кусочков и 8 цветных грядок.
# Каждая грядка обладает своей уникальной чертой - расстоянием, на которое необходимо
# бросить кусочек, чтобы он оказался в своей грядке. Ваша задача - написать скрипт, который с
# точностью и вниманием к деталям осуществит эти броски.
# Код победы: Как только все кусочки окажутся на своих грядках, появится код - символ вашего успеха и
# завершения задачи. Этот код необходимо будет ввести в поле для ответа, чтобы подтвердить вашу победу.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains


URL = "https://parsinger.ru/selenium/5.10/8/index.html"


# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)

        elements = driver.find_elements(By.CLASS_NAME, "piece")
        targets = driver.find_elements(By.CLASS_NAME, "range")

        for element, target in zip(elements, targets):
            actions.drag_and_drop(element, target).perform()

        result = wait.until(EC.element_to_be_clickable((By.ID, "message"))).text

        if result:
            print(result)


get_result(URL)
