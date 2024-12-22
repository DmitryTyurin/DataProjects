# Инициализация: Откройте заданный веб-сайт с помощью Selenium.
# Множественная навигация:
# На сайте есть 5 разных окон, в каждом из которых подгружается по 100 элементов при скроллинге.
# Техника скроллинга: Для каждого окна прокрутите страницу до самого низа.
# Здесь можно использовать ActionChains для эффективного скроллинга.
# Сбор информации: Из каждого окна извлеките все числовые значения и сложите их.
# Суммируйте данные из всех окон.
# Отправка результата: Вставьте полученную сумму в соответствующее поле для ответа на сайте.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://parsinger.ru/infiniti_scroll_3/"

# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        for i in range(1, 6):

            scroll_element = driver.find_element(
                By.ID, f"scroll-container_{i}"
            ).find_element(By.TAG_NAME, "div")

            result = 0

            for _ in range(10):
                actions = ActionChains(driver)
                actions.move_to_element(scroll_element)
                actions.scroll_by_amount(0, 500)
                actions.perform()

            p_elements = driver.find_elements(By.TAG_NAME, "span")

            for i in p_elements:
                text = i.text
                if text.isdigit():
                    result += int(text)

        print(result)


get_result(URL)
