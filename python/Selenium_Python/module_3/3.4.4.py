# Точка Входа: Откройте заданный веб-сайт с помощью Selenium.
# Сканирование: Используйте метод .find_elements() для поиска всех доступных полей для ввода на странице.
# Ввод данных: В цикле, переберите все найденные поля и заполните их с помощью метода .send_keys("Текст").
# Инициация: Найдите кнопку на странице и нажмите на неё.
# Результат: Скопируйте текст, который появится на экране рядом с кнопкой, если вы уложились в трёх секундный интервал.
# Фиксация: Запишите результат в отдельную переменную или вставьте ответ в поле ответа степик.

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://parsinger.ru/selenium/1/1.html"

data = ["Иванов", "Иван", "Иванович", 30, "Иваново", "ivanov@ivan.ru"]


def filling_forms(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        input_form = driver.find_elements(By.CLASS_NAME, "form")

        for d, f in enumerate(input_form):
            f.send_keys(data[d])

        driver.find_element(By.ID, "btn").click()

        print(driver.find_element(By.ID, "result").text)


filling_forms(URL)
