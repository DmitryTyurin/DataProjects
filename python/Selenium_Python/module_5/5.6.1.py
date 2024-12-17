# Прибытие на "Остров": Используйте Selenium для открытия заданного веб-сайта.
# Охота на Сокровище: В элементе с id="result" иногда появляется число — это и есть ваше сокровище. Проблема в том, что оно появляется очень редко.
# Вам придется обновлять страницу множество раз, пока не увидите это число.
# Клад в Руках: Как только число появится, скопируйте его и вставьте в предназначенное для этого поле ответа на вашем курсе.


from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://parsinger.ru/methods/1/index.html"


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        link = driver.find_element(By.ID, "result")
        text = link.text

        while True:
            result_link = driver.find_element(By.ID, "result")
            result_text = result_link.text

            driver.refresh()

            if result_text != text:
                print(result_text)

                break


get_result(URL)
