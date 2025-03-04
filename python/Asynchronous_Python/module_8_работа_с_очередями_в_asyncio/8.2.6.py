# Напишите асинхронный код, который моделирует процесс регистрации и приема пациентов в поликлинике.
# Сценарий включает в себя две ключевые функции: producer(), который регистрирует пациентов и добавляет их в очередь, и consumer(),
# который обрабатывает каждого пациента, имитируя процесс их приема врачом.

import asyncio

patient_info = [
    "Алексей Иванов: Прием для общего осмотра",
    "Мария Петрова: Чистка зубов",
    "Ирина Сидорова: Анализ крови",
    "Владимир Кузнецов: Рентгеновское исследование",
    "Елена Васильева: Вакцинация",
    "Дмитрий Николаев: Выписка рецепта",
    "Светлана Михайлова: Осмотр офтальмолога",
    "Никита Алексеев: Сеанс физиотерапии",
    "Ольга Сергеева: Срочный прием",
    "Анна Жукова: Регулярный контрольный осмотр",
]


async def producer(queue):
    for patient in patient_info:
        await asyncio.sleep(0.5)

        await queue.put(patient)
        print(f"Регистратор добавил в очередь: {patient}")

    await queue.put(None)


async def consumer(queue):
    while True:
        patient = await queue.get()

        if patient is None:
            queue.task_done()
            break

        await asyncio.sleep(0.5)
        print(f"Врач принял пациента: {patient}")

        queue.task_done()


async def main():
    queue = asyncio.Queue()

    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(producer(queue))
            tg.create_task(consumer(queue))

        await queue.join()
        consumer_task.cancel()

    except* Exception as e:
        [print(error) for error in e.exceptions]


asyncio.run(main())
