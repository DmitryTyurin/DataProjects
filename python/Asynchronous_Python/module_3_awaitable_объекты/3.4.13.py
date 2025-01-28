# Во всех предыдущих задачах вы имели дело с высокоуровневыми объектами класса Task и его методами (хотя все те же методы есть и у Future). Предлагаем вам задачу с использованием объектов Future и его особого метода - set_result().
#
# Этапы решения задачи:
#
# Допишите корутину waiter(future). Она должна ожидать завершения future (await future). После этого корутина должна вывести сообщение.
# f"future выполнен, результат {future.result()}. Корутина waiter() может продолжить работу"
# Допишите корутину setter(future). Она должна спать случайное время в интервале от 1 до 3 секунд. После этого установите результат для переданного future в значение True (метод set_result())
# В корутине main() создайте объект Future и одновременно запустите 2 задачи, одну для корутины waiter(future), одну для корутины setter(future) и дождитесь их выполнения (используйте asyncio.gather()).
# Комментарий к задаче.
#
# С помощью Future в данной задаче получается скоординировать работу 2-х задач. Для такой простой координации можно использовать и другие способы, например, просто последовательное выполнение задач, как в прошлом примере. Но если требуется более сложное взаимодействие между задачами, то лучше использовать Future или готовые классы и методы asyncio, которые преимущественно реализованы через объекты Future похожим способом.


import asyncio
import random


async def waiter(future):
    await future
    print(
        f"future выполнен, результат {future.result()}. Корутина waiter() может продолжить работу"
    )


async def setter(future):
    sleep_time = random.randint(1, 3)
    await asyncio.sleep(sleep_time)
    future.set_result(True)


async def main():
    future = asyncio.Future()
    tasks = [asyncio.create_task(waiter(future)), asyncio.create_task(setter(future))]
    await asyncio.gather(*tasks)


asyncio.run(main())
