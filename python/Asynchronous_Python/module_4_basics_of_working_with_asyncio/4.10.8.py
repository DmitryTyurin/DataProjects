# Корутина main() должна выводить на экран сообщение: "Корутина завершена".
# Корутина должна быть запущена с помощью метода loop.run_until_complete().
# При создании цикла событий вручную, сохраните его в переменную loop.
# Допишите функцию check_loop_status(loop) и запустите ее в трех местах так, чтобы вывод соотвествовал ожидаемому.
# Не забудьте закрыть цикл событий после завершения работы корутины.

import asyncio


async def main():
    print(check_loop_status(loop))
    print("Корутина завершена")


def check_loop_status(loop):
    return f"Цикл событий активен: {loop.is_running()}, Цикл событий закрыт: {loop.is_closed()}."


loop = asyncio.new_event_loop()
print(check_loop_status(loop))


loop.run_until_complete(main())


loop.close()
print(check_loop_status(loop))
