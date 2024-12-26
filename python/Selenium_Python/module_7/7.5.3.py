# Место преступления: Откройте указанный сайт с помощью Selenium.
# Улики на месте: На сайте вы найдете список пин-кодов. Однако среди них лишь один правильный.
# Расшифровка: Для проверки каждого пин-кода используйте кнопку "Проверить".
# При верном пин-коде вы получите секретный код.
# Доклад о проведенной работе: Вставьте полученный секретный код в специальное поле для на степик.
# Важные заметки
# Проанализировав обратную связь студентов, было выявлено,
# что многие из них делают одну и ту же ошибку при попытке отправить пин-код.
# Чтобы избежать этой ошибки, следуйте примеру ниже:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://parsinger.ru/selenium/5.8/3/index.html"

# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        pin_codes = driver.find_elements(By.CLASS_NAME, "pin")
        check = driver.find_element(By.ID, "check")

        for pin in pin_codes:
            extracted_text = pin.text

            check.click()

            alert = driver.switch_to.alert
            alert.send_keys(extracted_text)
            alert.accept()

            result = driver.find_element(By.ID, "result").text

            if result == "Неверный пин-код":
                pass
            else:
                print(result)


get_result(URL)
