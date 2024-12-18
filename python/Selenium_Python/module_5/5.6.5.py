# Запуск: Откройте основной сайт с помощью Selenium. С этой точки начнётся ваша экспедиция в поисках "Бессмертного Печенюшка".
# Следование за линками: На основной странице будет 42 ссылки.
# Открывайте каждую из них, чтобы исследовать и выяснить, какой из cookies имеет самый долгий срок жизни.
# Вычисление жизнеспособности: Для каждой открытой страницы анализируйте срок жизни её cookie ['expiry'].
# Сохраняйте эти данные для последующего сравнения.
# Коронация Бессмертного: После проверки всех 42 страниц определите, на какой из них находится cookie с самым долгим сроком жизни.
# С этой страницы извлеките число которое лежит в  теге <p id="result">INT</p>.
# Завершающий этап: Вставьте полученное число в специальное поле для степик.
# Поздравляем, вы нашли "Бессмертного Печенюшка" и преуспели в этой миссии!


from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://parsinger.ru/methods/5/index.html"


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        link_fields = driver.find_elements(By.TAG_NAME, "a")

        links = [l.get_attribute("href") for l in link_fields]

        expiry = 0
        result = 0

        for link in links:
            driver.get(link)
            cookies = driver.get_cookies()

            for cookie in cookies:
                if cookie["expiry"] > expiry:
                    expiry = cookie["expiry"]
                    result = driver.find_element(By.ID, "result").text

        print(result)


get_result(URL)
