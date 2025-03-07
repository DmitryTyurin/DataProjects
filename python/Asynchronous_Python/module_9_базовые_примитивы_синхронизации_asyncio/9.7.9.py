# Если кто-то из игроков в очереди на вход ждет больше 5 секунд, барьер надо сбросить и вывести для каждого ожидающего игрока сообщение

import asyncio

players = {
    "DragonSlayer": 0.2,
    "ShadowHunter": 0.6,
    "MagicWizard": 0.8,
    "ElfArcher": 2.0,
    "DarkMage": 1.4,
    "SteelWarrior": 1.6,
    "ThunderBolt": 3.0,
}


class DungeonExploration:
    def __init__(self, players: dict[str, float], part: int):
        self.players = players
        self.barrier = asyncio.Barrier(part)

    async def enter_dungeon(self, player: str, time: float):
        await asyncio.sleep(time)
        print(f"{player} готов войти в подземелье")

        try:
            await asyncio.wait_for(self.barrier.wait(), timeout=5)
            print(f"{player} вошел в подземелье")
        except (asyncio.TimeoutError, asyncio.BrokenBarrierError):
            print(f"{player} не смог попасть в подземелье. Группа не собрана")

    async def start(self):
        try:
            async with asyncio.TaskGroup() as tg:
                [
                    tg.create_task(self.enter_dungeon(player, time))
                    for player, time in self.players.items()
                ]
        except* Exception as e:
            [print(error) for error in e.exceptions]


tasks_run = DungeonExploration(players, 5)
asyncio.run(tasks_run.start())
