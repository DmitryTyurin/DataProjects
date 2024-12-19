# Инициализация: Используя Selenium, откройте заданный веб-сайт.
# Скроллинг: На сайте имеется список из 100 элементов, который расширяется при скроллинге (infinity scroll).
# Сбор данных: Скрольте по интерактивным элементам, чтобы раскрыть все 100 элементов списка.
# Используйте Keys.DOWN или методы ActionChains(driver).
# Агрегация: Извлеките все числовые значения из этих элементов и сложите их.
# Отправка ответа: Вставьте собранную сумму чисел в предназначенное поле на сайте.
# Помните о задержках при загрузке элементов.
# Последний элемент списка имеет класс last-of-list. Используйте это для прерывания цикла скроллинга.
# Внимательно изучите структуру HTML-страницы.
# Это поможет вам понять, как искать нужные элементы.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

URL = "https://parsinger.ru/infiniti_scroll_1/"

# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        action = ActionChains(driver)

        while True:
            last_child = driver.find_element(
                By.CSS_SELECTOR, ".scroll-container>span:last-child"
            )

            if last_child.get_attribute("class") == "last-of-list":
                break

            action.move_to_element(last_child).scroll_by_amount(0, 5000).perform()

        span = driver.find_elements(By.TAG_NAME, "span")

        result = 0

        for s in span:
            action.move_to_element(s).perform()
            s.find_element(By.TAG_NAME, "input").click()

            result += int(s.text)

            if s.get_attribute("class") == "last-of-list":
                break

        print(result)


get_result(URL)
