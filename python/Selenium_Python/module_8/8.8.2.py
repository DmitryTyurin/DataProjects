# Начало пути: Запустите браузер с помощью Selenium и посетите таинственный сайт.
# Терпение – ключ к успеху: Обратите внимание на кнопку, которая оживает после загрузки страницы.
# Время, которое потребуется для её активации, варьируется от 1 до 3 секунд.
# Секретные коды: Нажмите на кнопку, и начните слежение за заголовком страницы.
# Коды будут мелькать в этом заголовке с промежутками от 0,1 до 0,6 секунды.
# Открывайте глаза: Ваша цель - не просто просмотреть коды.
# Вам нужно отловить тот момент, когда в заголовке появится фраза "JK8HQ".
# Секретный знак: При обнаружении этой фразы в заголовке, используйте знакомый вам метод title_contains('JK8HQ').
# Если он вернет True, сохраните полный текст этого заголовка.
# Финальный шаг: Представьте найденный вами заголовок в качестве ответа на задачу.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://parsinger.ru/expectations/4/index.html"
TITLE_TEXT = "JK8HQ"

# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btn"))
        ).click()

        substring = WebDriverWait(driver, 30, poll_frequency=0.1).until(
            EC.title_contains(TITLE_TEXT)
        )
        if substring:
            print(driver.title)


get_result(URL)
