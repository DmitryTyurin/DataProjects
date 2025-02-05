# Создайте контекстную переменную order_state.
# Создайте обычную синхронную функцию для изменения значения контекстной переменной set_order_state(state), в которой будет изменяться значение контекстной переменной на то, которое передано в качестве аргумента.
# Напишите корутину process_order(), которая должна изменять состояние заказа в указанном порядке: "Принят", "Обрабатывается", "Отправлен". Для установки и изменения состояния заказа используйте функцию set_order_state(state).
# Добавьте задержку между изменением состояний, чтобы имитировать процесс обработки заказа (1 секунда перед каждым этапом).
# После каждого этапа выводите на экран сообщение: f"Заказ {order_id} сейчас в состоянии: {order_state}".
# В корутине main() одновременно запустите обработку заказов из списка orders, уже доступного в корутине main() и дождитесь их выполнения.


import asyncio
import contextvars

order_state = contextvars.ContextVar("order_state")


def set_order_state(state: str) -> None:
    order_state.set(state)


async def process_order(order_id: str) -> None:
    state_list = ["Принят", "Обрабатывается", "Отправлен"]

    for state in state_list:
        await asyncio.sleep(1)
        set_order_state(state)
        print(f"Заказ {order_id} сейчас в состоянии: {order_state.get()}")


async def main() -> None:
    orders = ["Заказ1", "Заказ123", "Заказ12345"]

    tasks = [asyncio.create_task(process_order(order)) for order in orders]

    gather = asyncio.gather(*tasks)
    await gather


asyncio.run(main())
