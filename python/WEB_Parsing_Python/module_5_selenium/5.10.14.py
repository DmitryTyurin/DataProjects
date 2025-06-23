# Первый Шаг: Откройте таинственный сайт с помощью Selenium,
# готовьтесь встретиться лицом к лицу с девятью рунными-стражами.
# Битва с Рекламой: Нажмите на любую кнопку, и как только это произойдет, перед вами появится назойливое рекламное окно.
# Ваша задача – быстро и решительно закрыть его, не давая ему нарушить ваш путь к секретам.
# Поиски Секретов: Как только реклама будет побеждена, обратите внимание на кнопку,
# которую вы только что освободили. На ней появятся подобные символы "01V5" – фрагмент древнего кода.
# Создание Ключа: Скопируйте символы и соберите из них длинный ключ в формате "YS93-R9R3-S019-PPI7-OS80-012C".
# Разделители "-" помогут вам организовать код и сделать его готовым к использованию.
# Порядок: Кликать можно в любом порядке, но собирать и "склеивать" его, необходимо в определённом порядке.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

URL = "https://parsinger.ru/selenium/5.9/5/index.html"


# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        elements = driver.find_elements(By.CLASS_NAME, "box_button")

        result = []

        for element in elements:
            element.click()

            driver.find_element(By.ID, "close_ad").click()

            wait = WebDriverWait(driver, 10)
            wait.until(lambda x: element.text)

            result.append(element.text)

        result = "-".join(result)

        print(result)


get_result(URL)
