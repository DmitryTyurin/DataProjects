# Мир слайдеров: Войдите на сайт с помощью Selenium, и вы окажетесь в мире, где 10 слайдеров ждут вашего внимания.
# Они как музыканты в оркестре, каждый из которых должен быть настроен точно, чтобы сыграть гармоничную мелодию.
# Задача точности: Ваша задача - внимательно и аккуратно передвинуть
# каждый слайдер на позицию, указанную в правом столбце.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


URL = "https://parsinger.ru/selenium/5.10/6/index.html"


# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)

        sliders = driver.find_elements(By.CLASS_NAME, "volume-slider")
        target_values = driver.find_elements(By.CLASS_NAME, "target-value")

        for slider, target in zip(sliders, target_values):
            current = int(slider.get_attribute("value"))
            target = int(target.text)

            if current < target:
                for x in range(target - current):
                    slider.send_keys(Keys.ARROW_RIGHT)
            elif current > target:
                for x in range(current - target):
                    slider.send_keys(Keys.ARROW_LEFT)

        result = wait.until(EC.element_to_be_clickable((By.ID, "message"))).text

        if result:
            print(result)


get_result(URL)
