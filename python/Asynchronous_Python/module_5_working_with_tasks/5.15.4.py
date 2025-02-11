# Вася решил создать свой собственный блог, в котором он будет публиковать свои мысли и идеи.
# Однако он не знает, как правильно организовать систему уведомлений о новых постах для своих подписчиков.
# Вася хочет, чтобы уведомления приходили всем подписчикам одновременно, и чтобы они не ждали слишком долго после публикации нового поста.

import asyncio

TEXT = "Hello world!"
SUBSCRIBERS_LIST = [
    "Alice",
    "Bob",
    "Charlie",
    "Dave",
    "Emma",
    "Frank",
    "Grace",
    "Henry",
    "Isabella",
    "Jack",
]


async def publish_post(text: str) -> None:
    await asyncio.sleep(1)
    print(f"Пост опубликован: {text}")


async def notify_subscribers(subscriber: str) -> None:
    print(f"Уведомление отправлено {subscriber}")


async def main(*args) -> None:
    text, subscribers = args

    task = asyncio.create_task(publish_post(text))
    done, pending = await asyncio.wait([task])

    for task in done:
        if task.done():
            try:
                async with asyncio.TaskGroup() as tg:
                    [
                        tg.create_task(notify_subscribers(subscriber))
                        for subscriber in subscribers
                    ]
            except* Exception as e:
                [print(error) for error in e.exceptions]
        else:
            print(f"Пост НЕ опубликован.")


asyncio.run(main(TEXT, SUBSCRIBERS_LIST))
