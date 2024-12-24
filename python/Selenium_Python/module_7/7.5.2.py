# Доступ к месту преступления: Используйте Selenium, чтобы получить доступ к веб-сайту, где спрятаны улики.
# Внимательное расследование: На сайте находится 100 кнопок.
# Каждая из них при нажатии активирует всплывающее alert окно с пин-кодом.
# Расшифровка: Под кнопками расположено текстовое поле, которое проверяет пин-коды.
# Ваша задача — ввести пин-код и проверить его. Если пин-код верный, вы получите секретный код.
# Завершение задачи: Вставьте полученный секретный код в специальное поле для ответа на степик.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://parsinger.ru/selenium/5.8/2/index.html"

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
            alert_text = alert.text
            alert.accept()

            driver.find_element(By.ID, "input").send_keys(alert_text)
            driver.find_element(By.ID, "check").click()

            result = driver.find_element(By.ID, "result").text

            if result == "Неверный пин-код":
                pass
            else:
                print(result)


get_result(URL)
