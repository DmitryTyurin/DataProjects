import asyncio

crew_list = [
    "smh547e3cebb1934a34a43d23bf31a96396",
    "smn9c88220fbeaa4c24aa6c8342d437618a",
    "smef64767c46d444c6c89937346c8cc4288",
    "sms_62933d018e09401bb61c3e823bdb4477",
]

bots = {
    "d234": "Пищевой синтезатор (утверждает, что готовка - дело настроения!):",
    "d235": "Робот-уборщик (неуклюжий, стеснительный, но ужасно старательный):",
    "d236": "Бар-робот (бывает, что пьет свои коктейли. И становится веселее!):",
    "d237": "Винтажный кибер-рассказчик (знает самые смешные анекдоты Галактики, все 20):",
    "d238": "Рембот №13 (уверен, что лучшее средство для ремонта - синяя изолента!):",
    "d239": "Несколько сварливый климат-контроль (а, вам бы так голову покрутили!):",
    "d240": "Дежурный медик-андроид (любит порассуждать о хрупкости человеческих организмов):",
    "d241": "Талисман экипажа кибер-кот Том (независим и самолюбив, как и положено настоящему коту):",
}


async def robot_reaction(event: asyncio.Event, bot: str, message: str):
    await event.wait()
    await speech_synt(bot, message)


async def _event(id: str, id_sm: str, event: asyncio.Event):
    if id == id_sm:
        await asyncio.sleep(2)
        event.set()
    else:
        print("Спокойно, ждем сержанта!")


async def birthday():
    id_sm = "sms_62933d018e09401bb61c3e823bdb4477"
    id_bots = ["d234", "d235", "d236", "d237", "d238", "d239", "d240", "d241"]
    message = "Повелитель механизмов! Долгих лет! Ты ведешь нас! Слава сержанту! Ура!"

    happy_event = asyncio.Event()

    bots_tasks = [robot_reaction(happy_event, bot, message) for bot in id_bots]

    await sensor_id_124(_event, id_sm, happy_event)

    await asyncio.gather(*bots_tasks)


async def speech_synt(bot: str, message: str):
    print(f"{bots.get(bot)}\n🌟🌟🌟{message}🌟🌟🌟")


async def sensor_id_124(fn, id_sm: str, event: asyncio.Event):
    for x in crew_list:
        await asyncio.sleep(0.5)
        await _event(x, id_sm, event)


asyncio.run(birthday())
