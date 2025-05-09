# Описание задачи:
#
# В Вашем распоряжении находится небольшая пиццерия, где работает команда талантливых поваров. Ваша задача - организовать процесс приготовления пиццы таким образом, чтобы использовать всего одну духовку, не нарушая рабочий процесс каждого повара. У каждого повара есть свой вид пиццы для приготовления, и время, необходимое для ее выпекания, строго определено.
#
# Синхронизируйте работу поваров с помощью блокировки так, чтобы духовка использовалась эффективно и без конфликтов.
#
# Шаги выполнения задачи:
#
# Изучите список поваров и список пицц, которые они должны приготовить. У каждой пиццы есть свое уникальное время приготовления.
#
# # Список имен поваров
# cooks_names = ["Алексей", "Марина", "Сергей", "Ирина", "Николай"]
# # Список видов пицц и время их приготовления
# pizzas = {
#     "Маргарита": 3,
#     "Пепперони": 2,
#     "Вегетарианская": 4,
#     "Четыре сыра": 5,
#     "Гавайская": 3
# }
# Используйте объект Lock для контроля доступа к духовке, чтобы гарантировать, что в любой момент времени духовкой может пользоваться только один повар.
#
# # Создаем объект мьютекса
# lock = threading.Lock()
# Создайте поток для каждого повара. В рамках потока каждый повар начинает приготовление своей пиццы, занимает духовку (блокирует Lock), готовит пиццу в течение необходимого времени, а затем освобождает духовку (разблокирует Lock), позволяя следующему повару начать свою работу.
#
# Выведите в консоль сообщения о начале и окончании приготовления каждой пиццы с указанием имени повара и названия пиццы, в правильном порядке.
#
# print(f'{name} начал(а) готовить пиццу "{pizza_name}".')
# print(f'{name} закончил(а) готовить пиццу "{pizza_name}".')
#
# print("Все пиццы приготовлены!")
#
#
# Технические детали:
#
# Используйте модуль threading для создания и управления потоками.
# Примените объект threading.Lock() для реализации блокировки, который будет контролировать доступ к духовке.
# Воспользуйтесь функцией time.sleep() для имитации времени, необходимого на приготовление пиццы.


from concurrent.futures import ThreadPoolExecutor
import threading
import time


class PizzaCook:
    def __init__(self):
        self.cooks_names = ["Алексей", "Марина", "Сергей", "Ирина", "Николай"]
        self.pizzas_data = {
            "Маргарита": 3,
            "Пепперони": 2,
            "Вегетарианская": 4,
            "Четыре сыра": 5,
            "Гавайская": 3,
        }
        self.pizzas_combined_data = dict(
            zip(self.cooks_names, self.pizzas_data.items())
        )
        self.lock = threading.Lock()
        self.executor = ThreadPoolExecutor(max_workers=5)

    def cooking(self):
        with self.lock:
            for name, (pizza_name, pizza_time) in self.pizzas_combined_data.items():
                print(f'{name} начал(а) готовить пиццу "{pizza_name}".')

                time.sleep(pizza_time / 10)
                print(f'{name} закончил(а) готовить пиццу "{pizza_name}".')

    def run(self):
        with self.executor as executor:
            futures = [executor.submit(self.cooking)]

            with self.lock:
                print("Все пиццы приготовлены!")


cook = PizzaCook()
cook.run()
