# Инициализация: Запустите браузер через Selenium и загрузите страницу.
# Настройка размеров: Откройте окно браузера так, чтобы рабочая (видимая) область страницы точно соответствовала 555x555 пикселям.
# Не забудьте учесть размеры рамок и панелей браузера при расчете!
# Анализ: Когда условие будет выполнено секретный ключ появится в id="result";
# Действие: Извлеките содержимое данного элемента и вставьте в поле для ответа.
# Подсказка: Убедитесь, что учли все элементы интерфейса браузера при настройке размера окна.
# Размеры рамок и панелей могут влиять на видимую область, и их необходимо учитывать в вашем решении.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://parsinger.ru/window_size/1/"

# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        win_size = 555

        def_width = driver.get_window_size()["width"]
        def_height = driver.get_window_size()["height"]

        work_width = driver.execute_script("return window.innerWidth;")
        work_height = driver.execute_script("return window.innerHeight;")

        diff_width = def_width - work_width
        diff_height = def_height - work_height

        driver.set_window_size(win_size + diff_width, win_size + diff_height)

        print(driver.find_element(By.ID, "result").text)


get_result(URL)
