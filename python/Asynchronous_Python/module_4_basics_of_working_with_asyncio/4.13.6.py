# Так действительно могло бы выглядеть асинхронное приложение до версии 3.7/3.8 с использованием декораторов @asyncio.coroutine и yield вместо async и await.
# Мы не сможем проверить отсутствие некоторых устаревших методов и приемов в вашем решении, но просим вас внимательно посмотреть на код и убрать те методы, которые не рекомендованы к использованию.
# А также избегайте использования низкоуровневых методов без необходимости, заменяя их на современные высокоуровневые.

import asyncio


async def send_message(message):
    print(f"Отправка сообщения: {message}")
    await asyncio.sleep(1)  # Имитация задержки отправки сообщения
    print(f"Сообщение отправлено: {message}")


async def receive_message():
    await asyncio.sleep(2)  # Имитация задержки получения сообщения
    message = "И тебе привет!"
    print(f"Сообщение получено: {message}")
    return message


async def main():
    send_task = asyncio.ensure_future(send_message("Привет"))
    receive_task = asyncio.ensure_future(receive_message())
    await asyncio.wait([send_task, receive_task])
    event_loop = asyncio.get_event_loop()
    print(f"Цикл событий активен: {event_loop.is_running()}")


asyncio.run(main())
