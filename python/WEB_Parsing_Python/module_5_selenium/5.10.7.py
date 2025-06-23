# Врата в Неизведанное: Ваше путешествие начнется с открытия сайта с помощью Selenium. На этом сайте вас ждет кнопка.
# Танец Элементов: После нажатия на эту кнопку, страница начнет игру с вами —
# на экране появится множество элементов с различными классами.
# Испытание Откровения: Среди этого множества элементов вашей задачей будет отыскать тот единственный,
# который мерцает классом "BMH21YY". Но не пытайтесь обмануть судьбу,
# делая это вручную — ваша цель — применить метод presence_of_element_located(locator)
# и дождаться момента его появления.
# Секретные Глифы: Как только этот таинственный элемент обнаружен, извлеките его содержимое и внесите в поле для ответа.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://parsinger.ru/expectations/6/index.html"
CLASS_TEXT = "BMH21YY"

# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btn"))
        ).click()

        result = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, CLASS_TEXT))
        )

        if result:
            print(result.text)


get_result(URL)