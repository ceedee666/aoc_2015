import random
from enum import Enum

Spells = Enum("Spells", ["MAGIC_MISSILE", "DRAIN", "SHIELD", "POISON", "RECHARGE"])

# spells
# cost, damage, heal, armor, mana, duration
SPELLS_DATA = {
    Spells.MAGIC_MISSILE: (53, 4, 0, 0, 0, 1),
    Spells.DRAIN: (73, 2, 2, 0, 0, 1),
    Spells.SHIELD: (113, 0, 0, 7, 0, 6),
    Spells.POISON: (173, 3, 0, 0, 0, 6),
    Spells.RECHARGE: (229, 0, 0, 0, 101, 5),
}


def available_spells(active_spells: dict[Spells, tuple], mana: int) -> list[Spells]:
    possible = [s for s in Spells if SPELLS_DATA[s][0] <= mana]
    for spell in active_spells:
        if active_spells[spell][5] > 1 and spell in possible:
            del possible[possible.index(spell)]
    return possible


def player_values(active_spells: dict[Spells, tuple]) -> tuple[int, int, int, int]:
    damage, health, armor, mana = 0, 0, 0, 0
    finished_spells = []
    for spell in active_spells:
        (
            _,
            spell_damage,
            spell_health,
            spell_armor,
            spell_mana,
            spell_duration,
        ) = active_spells[spell]
        spell_duration -= 1
        if spell_duration <= 0:
            finished_spells.append(spell)
        else:
            active_spells[spell] = (
                _,
                spell_damage,
                spell_health,
                spell_armor,
                spell_mana,
                spell_duration,
            )
        damage += spell_damage
        health += spell_health
        armor += spell_armor
        mana += spell_mana

    for spell in finished_spells:
        del active_spells[spell]
    return damage, health, armor, mana


def is_instant(spell: Spells) -> bool:
    return spell in [Spells.MAGIC_MISSILE, Spells.DRAIN]


def simulate_game(
    boss: tuple[int, int],
    player: tuple[int, int],
    player_mana: int = 500,
    hard: bool = False,
) -> tuple[bool, int]:
    active_spells = {}
    cost = 0
    player_health, player_damage = player
    boss_health, boss_damage = boss

    player_turn = True
    while True:
        if hard and player_turn:
            player_health -= 1
            if player_health <= 0:
                return False, cost

        if player_turn:
            available = available_spells(active_spells, player_mana)
            if not available:
                return False, cost

            spell = random.choice(available)

            player_mana -= SPELLS_DATA[spell][0]
            cost += SPELLS_DATA[spell][0]

            if is_instant(spell):
                active_spells[spell] = SPELLS_DATA[spell]

            damage, health, armor, mana = player_values(active_spells)

            if spell and not is_instant(spell):
                active_spells[spell] = SPELLS_DATA[spell]
        else:
            damage, health, armor, mana = player_values(active_spells)

        player_damage = damage
        player_health += health
        player_armor = armor
        player_mana += mana

        boss_health -= player_damage
        if boss_health <= 0:
            return True, cost

        if not player_turn:
            player_health -= max(1, boss_damage - player_armor)
            if player_health <= 0:
                return False, cost

        player_turn = not player_turn


def solve(boss: tuple[int, int], player: tuple[int, int], hard: bool = False) -> int:
    games = 5_000
    if hard:
        games *= 10

    return min(
        cost
        for win, cost in [simulate_game(boss, player, hard=hard) for _ in range(games)]
        if win
    )


if __name__ == "__main__":
    # health, damage
    boss = (55, 8)
    player = (50, 0)

    print("The least amount of mana needed is", solve(boss, player))
    print("The least amount of mana needed in hard mode is", solve(boss, player, True))
