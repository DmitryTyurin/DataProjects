# Идентификация Элемента: Первым делом необходимо найти элемент, с которым вы хотите взаимодействовать.
# Получение Фокуса: Воспользуйтесь методом scrollIntoView для того, чтобы прокрутить страницу так, чтобы нужный элемент оказался в видимой области.
# Клик по Элементу: Теперь, когда элемент в фокусе, попробуйте снова выполнить клик.
# Проверка Результата: Убедитесь, что ваше взаимодействие с элементом привело к желаемому результату(в теге с  <p id="result">788544</p> появляется уникальное для каждой кнопки число).
# Суммирование:  Суммируйте все полученные числа.
# Завершающий этап: Вставьте полученную сумму в поле ответов на Степике.


from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://parsinger.ru/scroll/4/index.html"

# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome(options_chrome) as driver:
        driver.get(url)

        elements = driver.find_elements(By.CLASS_NAME, "btn")

        result = 0

        for element in elements:
            driver.execute_script("return arguments[0].scrollIntoView(true);", element)
            element.click()

            number = int(driver.find_element(By.ID, "result").text)
            result += number

        print(result)


get_result(URL)
