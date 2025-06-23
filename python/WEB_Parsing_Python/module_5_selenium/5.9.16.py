# Откройте сайт с помощью selenium;
# У вас есть 2 списка с размера окон size_x и size_y;
# Цель: определить размер окна, при котором,  в id="result" появляется число;
# Результат должен быть в виде словаря {'width': size_x, 'height': size_y}
# ps. При написании кода, учитывайте размер рамок браузера.
# Метод .get_window_size() возвращает словарь с размерами окна.
# Размеры рамок могут зависеть от вашего разрешения и масштабирования экрана.
# Задача составлена при 100% масштабировании, масштабирование можно проверить в настройках дисплея.
# На вход ожидается словарь  {'width': 000, 'height': 000} где размеры указаны без учёта размеров рамок браузера,
# т.е. необходимо указать размер рабочей области браузера.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://parsinger.ru/window_size/2/index.html"

# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")

window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]


def get_result(url: str):
    with webdriver.Chrome() as driver:
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
                    print({"width": x, "height": y})


get_result(URL)
