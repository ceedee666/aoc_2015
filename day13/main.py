from collections import defaultdict
from itertools import permutations

from commons import read_input_file


def parse_input(
    lines: list[str], including_myself: bool
) -> tuple[set, dict[tuple[str, str], int]]:
    happiness = defaultdict(int)
    invited = set()
    for line in lines:
        parts = line.split(" ")
        invited.add(parts[0])
        a = parts[0]
        value = int(parts[3]) if parts[2] == "gain" else -int(parts[3])
        b = parts[10][:-1]
        happiness[(a, b)] = value

    if including_myself:
        invited.add("Myself")
    return invited, happiness


def calculate_happiness(seating: tuple, happiness: dict) -> int:
    return (
        sum(
            [
                happiness[(a, b)] + happiness[(b, a)]
                for (a, b) in zip(seating, seating[1:])
            ]
        )
        + happiness[(seating[0], seating[-1])]
        + happiness[(seating[-1], seating[0])]
    )


def solve(filename: str, including_myself: bool = False) -> int:
    lines = read_input_file(filename)
    invited, happiness = parse_input(lines, including_myself)
    return max([calculate_happiness(p, happiness) for p in permutations(invited)])


if __name__ == "__main__":
    print("The total change in happiness is", solve("input.txt"))
    print("The total change in happiness with myself is", solve("input.txt", True))
