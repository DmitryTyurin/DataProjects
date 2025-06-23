# Врата Веба: С помощью Selenium, откройте сайт, который является ареной вашего сражения.
# Баннер Ненависти: Как только страница откроется, вас встретит назойливый рекламный баннер,
# покрывающий собой содержимое сайта.
# Ваша цель — найти и нажать на крестик, чтобы закрыть этот баннер.
# Терпение и Внимание: Однако, этот баннер обладает способностью исчезать в течении длительно времени,
# не давая вашему скрипту добраться до цели сразу.
# Вам нужно проявить терпение и внимание, чтобы дождаться момента, когда баннер наконец исчезнет полностью.
# Используйте .invisibility_of_element_located() из прошлого степа, чтобы удостовериться в его исчезновении.
# Финальный Клик: После того как баннер исчезнет, ваш путь будет свободен. Найдите кнопку, которая теперь доступна
# для нажатия, и кликните по ней, чтобы раскрыть секретное значение.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://parsinger.ru/selenium/5.9/4/index.html"


# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        driver.find_element(By.CLASS_NAME, "close").click()

        wait = WebDriverWait(driver, 120)
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "close")))

        driver.find_element(By.TAG_NAME, "button").click()

        result = driver.find_element(By.ID, "message").text

        if result:
            print(result)


get_result(URL)
