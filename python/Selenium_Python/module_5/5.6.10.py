# Загрузка Страницы: Откройте страницу с помощью Selenium.
# Используйте эту страницу с двумя элементами для тренировки.
# Коды Цветов: Получите цвет в формате HEX из каждого элемента <span>.
# Выбор в Списке: В выпадающем списке в каждом контейнере найдите и выберите тот же HEX цвет что и у родительского контейнера.
# Кнопочная Магия: Найдите и нажмите на кнопку, у которой атрибут data-hex совпадает с HEX цветом родительского контейнера.
# Чек-Бокс Челлендж: Поставьте галочку в чек-боксе на странице.
# Текстовое Поле: Вставьте в текстовое поле тот же HEX-цвет, который имеет фон родительского контейнера.
# Подтверждение: Нажмите на кнопку "Проверить": если вставлен корректный HEX, то на кнопке появится "ОК".
# Повторение: Повторите все эти шаги для каждого найденного на странице контейнера.
# Финальный Шаг: После выполнения всех действий, нажмите на кнопку "Проверить все элементы", кнопка расположена в самом низу,
# появится alert если все условия соблюдены.
# Секретный Код: Из алерт-окна получите числовой код и вставьте его в поле ответа степик.


from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://parsinger.ru/selenium/5.5/5/1.html"

# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        main_container = driver.find_elements(By.CSS_SELECTOR, "#main-container > div")

        for c in main_container:
            color = c.find_element(By.TAG_NAME, "span").text

            c.find_element(By.CSS_SELECTOR, f'option[value="{color}"]').click()
            c.find_element(By.CSS_SELECTOR, f'button[data-hex="{color}"]').click()
            c.find_element(By.CSS_SELECTOR, '[type="checkbox"]').click()

            c.find_element(By.CSS_SELECTOR, '[type="text"]').send_keys(color)

            c.find_element(By.CSS_SELECTOR, "input + button").click()

        driver.find_element(By.CSS_SELECTOR, "body > button").click()

        alert = driver.switch_to.alert.text

        print(alert)


get_result(URL)
