# Инициализация: Используя Selenium, откройте заданный сайт.
# Анализ списков размеров: У вас есть два списка размеров – window_size_x и window_size_y.
# Тестирование: Примените каждое сочетание размеров из этих списков к окну вашего браузера.
# Поиск результата: После каждой установки размера проверяйте содержимое элемента с идентификатором id="result" на странице.
# Извлечение данных: Как только найдете уникальное сочетание, при котором на странице появляется число, скопируйте его и вставьте в поле для ответа.
# Подсказка: Размеры рамок и панелей браузера могут влиять на видимую область страницы.
# Убедитесь, что учли этот фактор при настройке размера окна.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://parsinger.ru/window_size/2/index.html"

window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome(options_chrome) as driver:
        driver.get(url)

        def_width = driver.get_window_size()["width"]
        def_height = driver.get_window_size()["height"]

        work_width = driver.execute_script("return window.innerWidth;")
        work_height = driver.execute_script("return window.innerHeight;")

        diff_width = def_width - work_width
        diff_height = def_height - work_height

        for x in window_size_x:
            for y in window_size_y:
                driver.set_window_size(x + diff_width, y + diff_height)
                result = driver.find_element(By.ID, "result").text

                if result:
                    print(result)


get_result(URL)
