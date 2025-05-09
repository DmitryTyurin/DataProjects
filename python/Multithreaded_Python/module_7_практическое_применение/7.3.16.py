# Описание задачи:
#
# Ваша задача - проверить безопасность системы путем поиска уникального кода среди множества возможных комбинаций. Ваш инструмент - мощь многопоточности и обработка исключений, которые помогут вам эффективно найти эталонный код среди тысяч возможных вариантов.
#
# elements = ["#fW", "^1a", "!b2", "l(3", "#5R", "e%1", "3Ff", "=b1", "vF^", "-F0"]
# Шаги выполнения задачи:
#
# Изучите предоставленный список elements, содержащий трехзначные коды. Ваша цель - создать все возможные комбинации этих кодов, формируя декартово произведение каждого элемента списка с каждым другим элементом, включая самого себя, три раза подряд(т.е. для одной итерации должен получится девятисимвольный элемент).
# Пример для первых элементов:
#
# #fW#fW#fW
# #fW#fW^1a
# #fW#fW!b2
# #fW#fWl(3
# #fW#fW#5R
# ...
# ...
# ...
#
#
# Под капотом задачи скрыта функция compare_element(element), которая сравнивает каждый сгенерированный элемент с заранее определенным эталонным кодом.
#
# compare_element()
#
# Если элемент совпадает с эталоном, функция возвращает сообщение о совпадении.
#
# return f"Элемент совпал = {element}"
# В противном случае, функция генерирует исключение, сообщая, что элемент не совпадает.
#
#  raise ValueError(f"Элемент {element} не совпадает с эталоном.")
# Используйте ThreadPoolExecutor для параллельной обработки каждого элемента декартова произведения.
#
# Для каждого задания, созданного в пуле потоков, обрабатывайте исключения, возникающие при сравнении элементов. Выводите сообщения об ошибках для элементов, которые не совпадают с эталоном, и отмечайте удачные совпадения.
#
# Вывод вашего кода должен быть примерно следующим:
#
# ...
# ...
# ...
# Элемент vF^=b1!b2 не совпадает с эталоном.
# Элемент vF^=b1l(3 не совпадает с эталоном.
# Элемент совпал = [значение скрыто]
# Элемент vF^=b1=b1 не совпадает с эталоном.
# Элемент vF^=b1vF^ не совпадает с эталоном.
# ...
# ...
# ...

from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from itertools import product

elements = ["#fW", "^1a", "!b2", "l(3", "#5R", "e%1", "3Ff", "=b1", "vF^", "-F0"]
combinations = list(product(elements, repeat=3))
formatted_combinations = ["".join(combination) for combination in combinations]


def lprint(text: str):
    lock: Lock = Lock()

    with lock:
        print(text)


def compare_element(element: str):
    # Эталонный элемент
    reference_element = "#fW#fW#fW"

    # Сравнение переданного элемента с эталоном
    if element == reference_element:
        return f"Элемент совпал = {element}"
    else:
        raise ValueError(f"Элемент {element} не совпадает с эталоном.")


def run():
    with ThreadPoolExecutor(max_workers=len(formatted_combinations)) as executor:
        futures = [
            executor.submit(compare_element, combination)
            for combination in formatted_combinations
        ]

        for future in futures:
            try:
                lprint(future.result())
            except ValueError as e:
                lprint(e)


run()
