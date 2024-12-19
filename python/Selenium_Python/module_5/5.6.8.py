# Случайная Локация: Откройте указанный сайт с помощью Selenium. Здесь вас встретят 100 текстовых полей, и рядом с некоторыми из них будут чекбоксы.
# Главная загвоздка: чекбоксы и их состояние ("checked" или нет) определяются случайным образом.
# Числовая Сборка: Пройдитесь по всем 100 текстовым полям и соберите числа только из тех, которые имеют рядом "checked" чекбоксы.
# Поля и чекбоксы могут загружаться в разных комбинациях, поэтому рассчитывать на конкретную последовательность или паттерн не стоит.
# Чекбоксы могут быть в двух состояниях: checked (отмечены) и unchecked (не отмечены). Мы интересуемся только числами из полей с отмеченными чекбоксами.
# Собранные числа необходимо суммировать и полученный результат вставить в поле ответа степик.


from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://parsinger.ru/selenium/5.5/3/1.html"

# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        elements = driver.find_elements(By.CLASS_NAME, "parent")

        result = 0

        for elem in elements:
            checkbox = elem.find_element(By.CLASS_NAME, "checkbox")

            if checkbox.is_selected():
                result += int(elem.find_element(By.TAG_NAME, "textarea").text)

        print(result)


get_result(URL)
