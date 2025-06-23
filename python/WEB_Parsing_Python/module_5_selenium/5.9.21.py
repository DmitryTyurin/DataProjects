# Подготовка: Загрузите список сайтов, на которых скрыты коды.
# Открытие вкладок: Используя Selenium, откройте каждый сайт в отдельной вкладке.
# Поиск кодов: Пройдитесь по всем вкладкам и найдите чекбокс. Нажмите на него, чтобы получить код.
# Обработка данных: Для каждого полученного кода найдите его квадратный корень.
# Суммирование: Сложите все полученные корни.
# Финальное преобразование: Округлите конечную сумму до 9 знаков после запятой.
# Результат: Вставьте полученное значение в поле для ответа.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

sites = [
    "http://parsinger.ru/blank/1/1.html",
    "http://parsinger.ru/blank/1/2.html",
    "http://parsinger.ru/blank/1/3.html",
    "http://parsinger.ru/blank/1/4.html",
    "http://parsinger.ru/blank/1/5.html",
    "http://parsinger.ru/blank/1/6.html",
]

# Добавляем аргумент для запуска браузера в фоновом режиме (без графического интерфейса)
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument("--headless=new")


def get_result():
    with webdriver.Chrome() as driver:

        result = 0

        for url in sites:
            driver.get(url)

            driver.find_element(By.CLASS_NAME, "checkbox_class").click()
            num = driver.find_element(By.ID, "result").text

            result += int(num) ** 0.5 if num.isnumeric() else 0

        print(round(result, 9))


get_result()
