# Исследование Территории: Откройте веб-сайт с помощью Selenium.
# Проанализируйте поля, с которыми предстоит работать.
# Миссия "Синхронизация": На странице находятся 100 текстовых полей: 50 серых и 50 синих.
# Ваша задача — перенести числа из серых полей в синие.
# Проверка и Контроль: Нажмите на кнопку "Проверить".
# Если перенос чисел прошёл успешно, поля станут зелёными.
# Получение Кода: Секретный код появится только в том случае, если все поля успешно стали зелёными.
# Секретный код нужно будет вставить в поле для ответа на степик.


from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://parsinger.ru/selenium/5.5/4/1.html"

# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        elements = driver.find_elements(By.CLASS_NAME, "parent")

        for elem in elements:
            color = elem.find_elements(By.TAG_NAME, "textarea")

            num = ""
            for i in color:
                if i.get_attribute("color") == "gray":
                    num = i.text
                    i.clear()
                if i.get_attribute("color") == "blue":
                    i.send_keys(num)

            elem.find_element(By.TAG_NAME, "button").click()

        driver.find_element(By.ID, "checkAll").click()

        result = driver.find_element(By.ID, "congrats").text

        print(result)


get_result(URL)
