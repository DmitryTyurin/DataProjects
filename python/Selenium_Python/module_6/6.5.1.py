# Инициализация: Откройте заданный веб-сайт с помощью Selenium.
# Обнаружение чекбоксов: На сайте будет 100 чекбоксов. Если кликнуть на чекбокс, может появится число в теге span
# Вычисление: Соберите все эти числа и сложите их.
# Отправка ответа: Введите сумму всех чисел, в поле ответа на Stepik.


from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://parsinger.ru/scroll/2/index.html"

# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        elements = driver.find_elements(By.CLASS_NAME, "item")
        result = 0

        for element in elements:
            element.find_element(By.CLASS_NAME, "checkbox_class").click()
            num = element.find_element(By.TAG_NAME, "span").text

            result += int(num) if num.isdigit() else 0

        print(result)


get_result(URL)
