# Вход в Цифровой Лабиринт: Используйте Selenium для открытия указанного веб-сайта.
# Извлечение Фрагментов: Найдите и извлеките данные из каждого второго тега <p> на странице.
# Воссоздание Артефакта: Просуммируйте все числовые значения, полученные из этих тегов.
# Ключ к Загадке: Запишите полученную сумму в предназначенное для этого поле или выведите на экран.


from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://parsinger.ru/selenium/3/3.html"


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        elements = driver.find_elements(By.XPATH, "//div[@class='text']/p[2]")
        print(elements)

        result = 0
        for elem in elements:
            n = int(elem.text)
            result += n

        print(result)


get_result(URL)
