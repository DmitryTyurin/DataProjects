# Откройте сайт с помощью Selenium.
# Найдите все четыре кнопки на странице.
# Определите значение value каждой кнопки. Это время, которое необходимо удерживать кнопку.
# Как только все кнопки станут зелёными, вы получите сообщение в alert. Скопируйте это сообщение.
# Вставьте полученное сообщение в поле ответа на Stepik.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://parsinger.ru/selenium/5.7/5/index.html"

# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        elements = driver.find_elements(By.CLASS_NAME, "timer_button")

        action = ActionChains(driver)

        for element in elements:
            action.click_and_hold(element)
            action.pause(float(element.text))
            action.release(element)
            action.perform()

        alert = driver.switch_to.alert
        print(alert.text)


get_result(URL)