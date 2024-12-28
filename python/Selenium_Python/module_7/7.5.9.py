# Погружение в кибермир: Используя Selenium, перейдите на указанный сайт.
# Поиск зеркальных комнат: На сайте вы обнаружите 9 iframe. В каждом из них скрыта кнопка.
# Сбор информации: Нажмите на кнопку в каждом iframe, чтобы получить число.
# Но помните, с вероятностью 1/9 это число окажется тем самым ключом к сейфу.
# Открытие тайны: Вставьте полученное число в поле для проверки.
# Если удача на вашей стороне, то это число откроет перед вами секретный код в alert.
# Вставьте полученный код из alert в поле ответа степик.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

URL = "https://parsinger.ru/selenium/5.8/5/index.html"

# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        input_btn = driver.find_element(By.ID, "guessInput")
        check_btn = driver.find_element(By.ID, "checkBtn")

        iframes = driver.find_elements(By.TAG_NAME, "iframe")

        codes = []

        for i in iframes:
            driver.switch_to.frame(i)
            driver.find_element(By.TAG_NAME, "button").click()

            codes.append(driver.find_element(By.ID, "numberDisplay").text)
            driver.switch_to.default_content()

        for code in codes:
            input_btn.clear()
            input_btn.send_keys(code)
            check_btn.click()

        alert_text = driver.switch_to.alert.text

        if alert_text:
            print(alert_text)


get_result(URL)
