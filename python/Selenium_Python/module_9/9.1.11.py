# Мир цветов: Войдите на указанный сайт с помощью Selenium, где вас встретят яркие, цветные шарики,
# каждый из которых ждёт своей очереди, чтобы оказаться в своём уютном контейнере.
# Задача сортировки: Ваша миссия - написать скрипт, который поможет каждому шарику найти его дом,
# соответствующий по цвету блок. Используйте свои знания и умения, чтобы аккуратно
# и внимательно перенести каждый шарик в его контейнер.
# Секретное сообщение: Как только последний шарик опустится в свой блок, на сцене появится секретное сообщение.
# Это сообщение - символ вашей победы, вашего умения создавать порядок из хаоса и находить гармонию в мире цветов.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains


URL = "https://parsinger.ru/selenium/5.10/4/index.html"


# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)

        balls = driver.find_elements(By.CLASS_NAME, "ball_color")
        baskets = driver.find_elements(By.CLASS_NAME, "basket_color")

        for ball in balls:
            ball_color = ball.value_of_css_property("background-color")

            for basket in baskets:
                basket_color = basket.value_of_css_property("background-color")

                if ball_color == basket_color:
                    actions.drag_and_drop(ball, basket).perform()

        result = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "message"))).text

        if result:
            print(result)


get_result(URL)
