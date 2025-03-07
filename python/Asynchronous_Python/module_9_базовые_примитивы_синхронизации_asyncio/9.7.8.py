# Ваша задача формировать группы по 5 человек с помощью asyncio.Barrier.
# Корутина enter_dungeon() должна ожидать время, указанное для каждого игрока, а затем вставать в очередь на ожидание с помощью барьера.
# Как только игрок добирается до подземелья и встает в очередь, программа должна выводить сообщение:

import asyncio

players = {
    "DragonSlayer": 0.2,
    "ShadowHunter": 0.6,
    "MagicWizard": 0.8,
    "KnightRider": 0.3,
    "ElfArcher": 2.0,
    "DarkMage": 1.4,
    "SteelWarrior": 1.6,
    "ThunderBolt": 3.0,
    "SilentAssassin": 1.1,
    "FireSorcerer": 2.6,
    "MysticHealer": 1.5,
    "IceQueen": 1.7,
    "BladeMaster": 2.9,
    "StormBringer": 1.2,
    "ShadowKnight": 0.9,
    "GhostRogue": 1.8,
    "FlameWielder": 0.7,
    "ForestGuardian": 0.4,
    "BattlePriest": 1.9,
    "EarthShaker": 2.8,
}


async def enter_dungeon(
    barrier: asyncio.Barrier, player: str, wait_time: float
) -> None:
    await asyncio.sleep(wait_time)
    print(f"{player} готов войти в подземелье")

    await barrier.wait()
    print(f"{player} вошел в подземелье")


async def main():
    barrier = asyncio.Barrier(5)

    try:
        async with asyncio.TaskGroup() as tg:
            [
                tg.create_task(enter_dungeon(barrier, player, wait_time))
                for player, wait_time in players.items()
            ]
    except* Exception as e:
        [print(error) for error in e.exceptions]


asyncio.run(main())
