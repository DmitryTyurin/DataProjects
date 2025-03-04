# Напишите асинхронный код для распределения пациентов по специалистам-врачам в медицинском центре.
# Код должен управлять очередями пациентов, где каждый пациент имеет направление к врачу определенного профиля. Всего должно быть 3 очереди.

import asyncio

patient_info = [
    {
        "name": "Алексей Иванов",
        "direction": "Терапевт",
        "procedure": "Прием для общего осмотра",
    },
    {"name": "Мария Петрова", "direction": "Хирург", "procedure": "Малая операция"},
    {"name": "Ирина Сидорова", "direction": "ЛОР", "procedure": "Осмотр уха"},
    {"name": "Владимир Кузнецов", "direction": "Терапевт", "procedure": "Консультация"},
    {
        "name": "Елена Васильева",
        "direction": "Хирург",
        "procedure": "Хирургическая процедура",
    },
    {"name": "Дмитрий Николаев", "direction": "ЛОР", "procedure": "Промывание носа"},
    {
        "name": "Светлана Михайлова",
        "direction": "Терапевт",
        "procedure": "Рутинный осмотр",
    },
    {
        "name": "Никита Алексеев",
        "direction": "Хирург",
        "procedure": "Операция на колене",
    },
    {"name": "Ольга Сергеева", "direction": "ЛОР", "procedure": "Лечение ангины"},
    {"name": "Анна Жукова", "direction": "Терапевт", "procedure": "Вакцинация"},
]

queues = {
    "Терапевт": asyncio.Queue(),
    "Хирург": asyncio.Queue(),
    "ЛОР": asyncio.Queue(),
}


async def producer(patient_info):
    for patient in patient_info:
        await asyncio.sleep(0.5)

        direction = patient.get("direction")

        await queues[direction].put(patient)
        print(
            f"Регистратор добавил в очередь: {patient['name']}, направление: {patient['direction']}, процедура: {patient['procedure']}"
        )


async def consumer(queue, doctor_type):
    while True:
        patient = await queue.get()

        await asyncio.sleep(0.5)
        print(
            f"{doctor_type} принял пациента: {patient['name']}, процедура: {patient['procedure']}"
        )

        queue.task_done()


async def main():
    queue = asyncio.Queue()

    try:
        async with asyncio.TaskGroup() as tg:
            producer_task = tg.create_task(producer(patient_info))
            consumer_tasks = [
                asyncio.create_task(consumer(queue, doctor_type))
                for doctor_type, queue in queues.items()
            ]

        [await queue.join() for queue in queues.values()]

        [task.cancel() for task in consumer_tasks]

    except* Exception as e:
        [print(error) for error in e.exceptions]


asyncio.run(main())
