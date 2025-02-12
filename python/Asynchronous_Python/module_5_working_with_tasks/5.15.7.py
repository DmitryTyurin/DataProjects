# Задание:  Написать асинхронный код, который будет модерировать список сообщений.
# Каждое сообщение представляет собой словарь с двумя полями: message_id и message.
# Ваша задача - проверить каждое сообщение на наличие запрещенных слов, не учитывая регистр букв, используйте метод lower().

import asyncio
import re

banned_words = [
    "ошибка",
    "баг",
    "отладка",
    "память",
    "процессор",
    "компиляция",
    "алгоритм",
    "функция",
    "база данных",
    "интерфейс",
]

message = [
    {
        "message_id": 45677,
        "message": "Я думаю, мы должны рассмотреть новый алгоритм для этого задания.",
    },
    {"message_id": 66994, "message": "У нас есть ошибка в последнем коммите."},
    {
        "message_id": 61982,
        "message": "Мне кажется, мы можем оптимизировать использование памяти.",
    },
    {
        "message_id": 24766,
        "message": "У нас проблемы с базой данных на продакшн сервере.",
    },
    {"message_id": 78228, "message": "Стоит ли рассмотреть отладку этого кода?"},
    {"message_id": 59949, "message": "Проблема с процессором на сервере B."},
    {"message_id": 15427, "message": "Баг был найден в последней версии кода."},
    {"message_id": 71942, "message": "Я сейчас занимаюсь компиляцией новой версии."},
    {
        "message_id": 69061,
        "message": "Интерфейс этой системы довольно сложен для новичков.",
    },
    {
        "message_id": 15224,
        "message": "Не могу понять, в какой функции появляется этот баг.",
    },
    {"message_id": 33910, "message": "Твой код работает исключительно быстро."},
    {
        "message_id": 50394,
        "message": "Я нашел пару отличных статей о машинном обучении.",
    },
    {"message_id": 64023, "message": "Ты пользуешься Git для управления версиями?"},
    {"message_id": 27769, "message": "Мы сможем справиться с этим проектом в срок."},
    {
        "message_id": 20857,
        "message": "Расскажи мне о своем опыте использования Python.",
    },
    {"message_id": 85640, "message": "Какой твой любимый язык программирования?"},
    {"message_id": 63481, "message": "Я работал с Java до этого проекта."},
    {
        "message_id": 46548,
        "message": "Мы можем встретиться завтра, чтобы обсудить этот код.",
    },
    {
        "message_id": 47734,
        "message": "Стоит ли использовать TensorFlow для этого проекта?",
    },
    {"message_id": 66161, "message": "Можешь проверить мой код перед коммитом?"},
    {
        "message_id": 18595,
        "message": "Очень сложно находить ошибки в коде без должной документации.",
    },
    {
        "message_id": 96671,
        "message": "Всегда делай резервное копирование перед большими изменениями.",
    },
    {"message_id": 38870, "message": "Удивительно, как быстро развивается технология."},
    {"message_id": 36145, "message": "Стоит ли использовать Docker в этом проекте?"},
    {
        "message_id": 54105,
        "message": "Процессор сервера перегружен из-за большого количества запросов.",
    },
    {"message_id": 56691, "message": "У тебя есть опыт работы с Node.js?"},
    {
        "message_id": 59368,
        "message": "Я читаю книгу о криптографии, она очень интересная.",
    },
    {"message_id": 90083, "message": "Ты когда-нибудь работал с NoSQL базами данных?"},
    {"message_id": 26180, "message": "Давай попробуем разобраться с этим багом."},
    {
        "message_id": 63092,
        "message": "Я всегда любил математическую сторону программирования.",
    },
    {"message_id": 13559, "message": "Какой твой любимый способ отладки?"},
    {"message_id": 24649, "message": "Мы должны пересмотреть структуру базы данных."},
    {
        "message_id": 41506,
        "message": "Я прочитал твою документацию, она очень подробная.",
    },
    {
        "message_id": 73454,
        "message": "Какой у тебя опыт работы с облачными технологиями?",
    },
    {
        "message_id": 15405,
        "message": "Мне нравится работать с открытым исходным кодом.",
    },
    {
        "message_id": 95661,
        "message": "Нам нужен более эффективный алгоритм для решения этой задачи.",
    },
    {"message_id": 46595, "message": "Мы используем React для нашего фронтенда."},
    {
        "message_id": 90783,
        "message": "У нас возникла проблема с интерфейсом пользователя.",
    },
    {
        "message_id": 37029,
        "message": "Я заметил странное поведение функции в этом коде.",
    },
    {
        "message_id": 87001,
        "message": "Мы смогли ускорить код, оптимизировав использование памяти.",
    },
    {
        "message_id": 72243,
        "message": "Ваш код работает, но есть проблемы с производительностью.",
    },
    {
        "message_id": 59828,
        "message": "Я думаю, стоит добавить комментарии к этому коду.",
    },
    {
        "message_id": 73836,
        "message": "Нам стоит переписать эту функцию для улучшения производительности.",
    },
    {
        "message_id": 36427,
        "message": "Наш новый проект находится в активной стадии разработки.",
    },
    {"message_id": 87918, "message": "Мы смогли устранить этот баг."},
    {
        "message_id": 64104,
        "message": "Я всегда проверяю свой код на наличие утечек памяти.",
    },
    {"message_id": 43701, "message": "Ты когда-нибудь работал с Rust?"},
    {"message_id": 14183, "message": "Я думаю, что наша компиляция прошла успешно."},
    {
        "message_id": 42332,
        "message": "Все сервера работают стабильно, кроме одного, есть проблема с процессором.",
    },
    {
        "message_id": 52014,
        "message": "У нас есть новый инструмент для отладки, я думаю, он тебе понравится.",
    },
    {
        "message_id": 41863,
        "message": "Я думаю, это наша последняя ошибка, после ее исправления код будет работать идеально.",
    },
]


async def check_message(banned_list: list, message: str) -> bool:
    words = re.sub(r"[,.]", "", message)
    words = words.lower().split()

    for word in words:
        if word in banned_list:
            return False
    return True


async def process_message(banned_list: list, message_dict: dict) -> None:
    message = message_dict.get("message")
    message_id = message_dict.get("message_id")

    task = asyncio.current_task()
    try:
        if not await check_message(banned_list, message):
            task.cancel()
            print(f"В сообщении {message_id} стоп-слово: task.done(): {task.done()}")
            return

        print(f"{message_id}: {message}")

    except asyncio.CancelledError:
        print(f"Задача для сообщения {message_id} была отменена.")


async def main(banned_list: list, messages_list: list) -> None:
    try:
        async with asyncio.TaskGroup() as tg:
            [
                tg.create_task(process_message(banned_list, message))
                for message in messages_list
            ]
    except* Exception as e:
        [print(error) for error in e.exceptions]


asyncio.run(main(banned_words, message))
