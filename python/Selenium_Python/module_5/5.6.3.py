# Запустите ваш кибер-копатель и отправьтесь на заданный сайт.
# Особая задача сбора: Соберите только те "печеньки", значения которых имеют чётные числа после символа "_".
# Например, если cookie имеет имя "session_12", число "12" является чётным, и это именно то, что вам нужно.
# Анализ и суммирование: Суммируйте числовые значения этих особых "печенек". Это сумма будет вашим ключом.
# Ввод ответа: После расшифровки вставьте ваш ключ в специальное поле для ответов на степик.
# Успех здесь означает ваш переход на следующий уровень задания.


from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://parsinger.ru/methods/3/index.html"


def get_result(url: str):
    with webdriver.Chrome() as driver:
        driver.get(url)

        cookies = driver.get_cookies()

        sum_result = 0

        for cookie in cookies:
            cookie_num = int(cookie.get("name").split("_")[2])

            if cookie_num % 2 == 0:
                sum_result += int(cookie.get("value"))

        print(sum_result)


get_result(URL)
