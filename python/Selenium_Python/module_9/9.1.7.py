# Открытие мира: Используйте Selenium для того, чтобы ступить на порог виртуального пространства,
# где синий квадрат ожидает своего часа, чтобы начать своё путешествие.
# Синий путник и красные ориентиры: На вашем пути встретятся красные точки, которые будут служить
# ориентирами и проверочными пунктами. Ваша задача - написать скрипт, который возьмёт на себя роль проводника,
# и аккуратно и последовательно проведёт синий квадрат через все красные точки, следуя по оси X(слева направо).
# Появление токена: После того как последняя красная точка будет покорена, на экране появится токен -
# символ вашего успеха и точности в выполнении задачи.
# Завершение миссии: Вставьте полученный токен в поле для ответа, тем самым завершив своё путешествие и
# подтвердив свои навыки владения Selenium.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://parsinger.ru/draganddrop/3/index.html"


# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        block = driver.find_element(By.ID, "block1")
        points = driver.find_elements(By.CLASS_NAME, "controlPoint")
        action = ActionChains(driver)
        wait = WebDriverWait(driver, 10)

        for p in points:
            action.drag_and_drop_by_offset(block, 50, 0).perform()

        result = wait.until(EC.element_to_be_clickable((By.ID, "message"))).text

        if result:
            print(result)


get_result(URL)
