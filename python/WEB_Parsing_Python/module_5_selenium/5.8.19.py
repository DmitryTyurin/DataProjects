# Инициализация: Откройте заданный веб-сайт с помощью Selenium.
# Техника скроллинга: Сайт содержит список из 100 элементов, которые появляются только при скроллинге.
# Стандартные элементы типа чекбоксов или другие элементы для "зацепления" тут отсутствуют.
# Навигация: Прокрутите страницу до самого низа, используя ActionChains.
# Сбор информации: Извлеките все числовые значения из появившихся элементов и сложите их.
# Отправка результата: Вставьте полученную сумму в соответствующее поле для ответа на степик.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://parsinger.ru/infiniti_scroll_2/"

# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        scroll_element = driver.find_element(By.ID, "scroll-container").find_element(
            By.TAG_NAME, "div"
        )

        while True:
            result = 0

            actions = ActionChains(driver)
            actions.move_to_element(scroll_element)
            actions.scroll_by_amount(0, 500)
            actions.perform()

            p_elements = driver.find_elements(By.TAG_NAME, "p")

            for i in p_elements:
                text = i.text

                if text.isdigit():
                    result += int(text)

            try:
                if driver.find_element(By.CLASS_NAME, "last-of-list"):
                    break
            except:
                pass

        print(result)


get_result(URL)
