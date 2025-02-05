# Создайте контекстную переменную current_language.
# Создайте обычную функцию для изменения значения контекстной переменной set_language(language_code).
# Допишите корутины приветствия и сообщения об ошибке (get_greeting() и get_error_message()) так, чтобы они возвращали сообщение на том языке, код которого хранится в контекстной переменной (en, ru или es). Эти корутины не должны принимать никаких аргументов.
# Допишите корутину test_user_actions(language_code), которая будет в самом начале устанавливать значение контекстной переменной равным переданному в качестве аргумента, а затем выводить на экран приветственное сообщение и сообщение об ошибке.
# В корутине main() запустите тестирование test_user_actions(language_code) для каждого языка в таком порядке:
# en: английский
# ru: русский
# es: испанский

import asyncio
import contextvars

current_language = contextvars.ContextVar("current_language")


def set_language(language_code: str) -> None:
    current_language.set(language_code)


async def get_greeting():
    greetings = {"en": "Hello!", "ru": "Привет!", "es": "Hola!"}

    return greetings[current_language.get()]


async def get_error_message() -> str:
    error_messages = {
        "en": "An error occurred.",
        "ru": "Произошла ошибка.",
        "es": "Ocurrió un error.",
    }

    return error_messages[current_language.get()]


async def test_user_actions(language_code: str) -> None:
    set_language(language_code)
    print(await get_greeting())
    print(await get_error_message())


async def main() -> None:
    languages = ["en", "ru", "es"]

    tasks = [asyncio.create_task(test_user_actions(language)) for language in languages]

    gather = asyncio.gather(*tasks)
    await gather


asyncio.run(main())
