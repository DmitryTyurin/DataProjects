# Загрузка страницы: Откройте страницу с помощью Selenium.
#
# Используйте эту страницу с двумя элементами для тренировки.
#
# Коды цветов: Получите цвет в формате HEX из каждого элемента <span>.
#
# Выбор в списке: В выпадающем списке в каждом контейнере найдите и выберите тот же HEX цвет что и у родительского контейнера.
#
# Кнопочная магия: Найдите и нажмите на кнопку, у которой атрибут data-hex совпадает с HEX цветом родительского контейнера.
#
# Чек-бокс челлендж: Поставьте галочку в чек-боксе на странице.
#
# Текстовое поле: Вставьте в текстовое поле тот же HEX-цвет, который имеет фон родительского контейнера.
#
# Подтверждение: Нажмите на кнопку "Проверить": если вставлен корректный HEX, то на кнопке появится "ОК".
#
# Повторение: Повторите все эти шаги для каждого найденного на странице контейнера.
#
# Финальный шаг: После выполнения всех действий, нажмите на кнопку "Проверить все элементы", кнопка расположена в самом низу, появится alert если все условия соблюдены.
#
# Секретный код: Из алерт-окна получите числовой код и вставьте его в поле ответа степик.
#
# Примечания
# Внимательно следите за атрибутами элементов, чтобы правильно их выбрать.
# Код должен быть универсальным и работать со всеми найденными на странице элементами.

from selenium import webdriver
from selenium.webdriver.common.by import By


class DataDriver:
    def __init__(self):
        self.url = "https://parsinger.ru/selenium/5.5/5/1.html"
        self.options = self.setup_options()
        self.driver = webdriver.Chrome(options=self.options)

    @staticmethod
    def setup_options():
        from selenium.webdriver.chrome.options import Options

        options = Options()
        # options.add_argument("--headless")  # Без графического интерфейса
        # options.add_argument('--disable-gpu')  # Отключаем GPU
        options.add_argument("--window-size=1920,1080")  # Устанавливаем размер окна

        return options

    def get_result(self, driver, url):
        import time

        driver.get(url)

        elements = driver.find_elements(By.CSS_SELECTOR, "#main-container > div")

        for element in elements:
            color = element.find_element(By.TAG_NAME, "span").text

            element.find_element(By.CSS_SELECTOR, f'option[value="{color}"]').click()
            element.find_element(By.CSS_SELECTOR, f'button[data-hex="{color}"]').click()
            element.find_element(By.CSS_SELECTOR, '[type="checkbox"]').click()
            element.find_element(By.CSS_SELECTOR, '[type="text"]').send_keys(color)
            element.find_element(By.CSS_SELECTOR, "input + button").click()

        driver.find_element(By.CSS_SELECTOR, "body > button").click()

        result = self.get_alert_text(driver)

        return result

    @staticmethod
    def get_alert_text(driver):
        alert = None
        alert_text = None

        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
        except Exception as e:
            print(f"Всплывающее окно не найдено: {e}")
        finally:
            if alert:
                alert.accept()

        return alert_text

    def run(self):
        with self.driver as driver:
            data = self.get_result(driver, self.url)

            print(data)


def main():
    d = DataDriver()
    d.run()


main()
