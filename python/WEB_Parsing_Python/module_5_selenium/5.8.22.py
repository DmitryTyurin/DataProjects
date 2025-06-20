# Инициализация: Откройте заданный веб-сайт с помощью Selenium.
# Бесконечный Скроллинг: На сайте есть блок с бесконечной подгрузкой чекбоксов.
# Всего 100 контейнеров и в каждом контейнере 10 чек боксов.
# Чётный Выбор: Устанавливайте чекбоксы только с чётным значением атрибута value
# Алерт-Кнопка: После установки всех чекбоксов во всех контейнерах кнопка alert с классом alert_button.
# Нажмите на неё, чтобы вызвать сообщение alert , в alert и будет ключ к решению задачи.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://parsinger.ru/selenium/5.7/4/index.html"

# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        action = ActionChains(driver)

        while True:
            last_child = driver.find_element(
                By.CSS_SELECTOR, "#main_container div:last-child"
            )

            action.move_to_element(last_child).scroll_by_amount(0, 5000).perform()

            elements = driver.find_elements(By.CLASS_NAME, "child_container")
            if len(elements) == 100:
                break

        for element in elements:
            input_elements = element.find_elements(By.TAG_NAME, "input")

            for i in input_elements:
                if int(i.get_attribute("value")) % 2 == 0:
                    i.click()

        driver.find_element(By.CLASS_NAME, "alert_button").click()
        alert_text = driver.switch_to.alert.text

    print(alert_text)


get_result(URL)