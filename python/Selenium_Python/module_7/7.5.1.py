# Запуск: Откройте указанный веб-сайт с использованием Selenium.
# Исследование: На странице размещено 100 кнопок.
# Отправьтесь в путешествие, кликая по каждой из них, чтобы понять, какая из них прячет желаемый код.
# Обнаружение: При активации правильной кнопки, секретный код появится в теге: <p id="result">Code</p>.
# Финальный штрих: Скопируйте этот код и вставьте его в специальное поле для ответа на степик.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://parsinger.ru/selenium/5.8/1/index.html"

# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        elements = driver.find_elements(By.CLASS_NAME, "buttons")

        for element in elements:
            element.click()

            alert = driver.switch_to.alert
            alert.accept()

            result = driver.find_element(By.ID, "result").text

            print(result)


get_result(URL)
