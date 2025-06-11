# Добро пожаловать в лабораторию мастера заполнения форм! Перед вами стоит непростая задача: вскрыть виртуальный сейф, заполнить поля аутентификации и взять "ключ", который появляется на экране. И конечно же, это нужно сделать всё в течение трёх секунд. Научимся пользоваться инструментами хакера в лучших традициях Hollywood, но в нашем случае всё будет законно и для образовательных целей!
#
# Основные Этапы:
# Точка входа: Откройте заданный веб-сайт с помощью Selenium.
# Сканирование: Используйте метод .find_elements() для поиска всех доступных полей для ввода на странице.
# Ввод данных: В цикле, переберите все найденные поля и заполните их с помощью метода .send_keys("Текст").
# Инициация: Найдите кнопку на странице и нажмите на неё.
# Результат: Скопируйте текст, который появится на экране рядом с кнопкой, если вы уложились в трёхсекундный интервал.
# Фиксация: Запишите результат в отдельную переменную или вставьте ответ в поле ответа степик.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/1/1.html"
        self.driver = webdriver.Chrome()
        self.input_list = [
            "Иванов",
            "Иван",
            "Иванович",
            30,
            "Иваново",
            "ivanov@ivan.ru",
        ]

    def input_data(self, driver, url):
        driver.get(url)

        form_box = driver.find_elements(By.CLASS_NAME, "form")

        for item, box in enumerate(form_box):
            box.send_keys(self.input_list[item])

        driver.find_element(By.ID, "btn").click()
        data = driver.find_element(By.ID, "result").text

        return data

    def run(self):
        with self.driver as driver:
            result = self.input_data(driver, self.url)

            print(result)


def main():
    d = DataDriver()
    d.run()


main()
