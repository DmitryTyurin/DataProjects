# Портал В Неизвестное: Ваш первый шаг - зайти на сайт и стать свидетелем этого волшебства:
# блоки появляются и исчезают, как призраки.
# Легенда о Таинственном Блоке: Среди множества блоков есть один особенный.
# Его ID "qQm9y1rk", и он – ключ к забытым знаниям.
# Сражение с Временем: Проблема в том, что никто не знает, когда и где этот блок решит показать себя.
# Он может мелькнуть на долю секунды или вовсе остаться в тени. Но если вы его увидите, действуйте быстро!
# Ключевой Момент: Как только вы обнаружите блок с ID "qQm9y1rk", мгновенно кликните по нему.
# Ведь этот блок не привык к вниманию и быстро исчезнет.
# Сокровище Знаний: Если вам удастся кликнуть по блоку, вы будете вознаграждены:
# в alert-окне появится секретный код, который приведет вас к решению задачи.
# Совет: Не дайте себя увлечь этим магическим балетом блоков.
# Сосредоточьтесь на своей цели, и сокровище будет вашим!

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://parsinger.ru/selenium/5.9/2/index.html"
ID_NAME = "qQm9y1rk"

# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        elem_loc = (By.ID, ID_NAME)

        wait = WebDriverWait(driver, 120, poll_frequency=0.1)
        wait.until(EC.presence_of_element_located(elem_loc)).click()

        print(driver.switch_to.alert.text)


get_result(URL)