from itertools import combinations, product
from math import ceil

# Cost, Damage, Armor
WEAPONS = {
    "dagger": (8, 4, 0),
    "shaortsword": (10, 5, 0),
    "waarhammer": (25, 6, 0),
    "loangsword": (40, 7, 0),
    "graeataxe": (74, 8, 0),
}

ARMORS = {
    "none": (0, 0, 0),
    "leather": (13, 0, 1),
    "chainmail": (31, 0, 2),
    "splintmail": (53, 0, 3),
    "bandedmail": (75, 0, 4),
    "platemail": (102, 0, 5),
}
RINGS = {
    "none 1": (0, 0, 0),
    "none 2": (0, 0, 0),
    "damage +1": (25, 1, 0),
    "damage +2": (50, 2, 0),
    "damage +3": (100, 3, 0),
    "defense +1": (20, 0, 1),
    "defense +2": (40, 0, 2),
    "defense +3": (80, 0, 3),
}

# health, damage, armor
BOSS = (103, 9, 2)


def is_winning(
    combination: tuple[str, str, tuple[str, ...]], health, boss_is_winning
) -> bool:
    weapon, armor, rings = combination
    damage_value = WEAPONS[weapon][1] + sum([RINGS[ring][1] for ring in rings])
    armor_value = ARMORS[armor][2] + sum([RINGS[ring][2] for ring in rings])

    turns = ceil(BOSS[0] / max(damage_value - BOSS[2], 1))
    boss_turns = ceil(health / max(BOSS[1] - armor_value, 1))
    if boss_is_winning:
        return turns > boss_turns
    else:
        return turns <= boss_turns


def costs(combination: tuple[str, str, tuple[str, ...]]) -> int:
    weapon, armor, rings = combination
    return (
        WEAPONS[weapon][0] + ARMORS[armor][0] + sum([RINGS[ring][0] for ring in rings])
    )


def solve(health=100, boss_is_winning=False):
    possible_combinations = product(WEAPONS, ARMORS, combinations(RINGS, 2))
    winning_combinations = [
        c for c in possible_combinations if is_winning(c, health, boss_is_winning)
    ]
    combination_costs = [costs(c) for c in winning_combinations]
    if boss_is_winning:
        return max(combination_costs)
    else:
        return min(combination_costs)


if __name__ == "__main__":
    print("The minimal amount of gold to spend and still win is", solve())
    print(
        "The maximal amount of gold to spend and still lose is",
        solve(boss_is_winning=True),
    )
