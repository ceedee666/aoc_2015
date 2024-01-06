from collections import defaultdict

from commons import read_input_file

TICKER_TAPE = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def parse_input(lines: list[str]) -> defaultdict:
    aunts = defaultdict(lambda: defaultdict(lambda: -1))
    for line in lines:
        idx = line.find(":")
        name = line[:idx]
        compounds = line[idx + 2 :].split(", ")
        for compound in compounds:
            category, value = compound.split(": ")
            value = int(value)
            aunts[name][category] = value
    return aunts


def solve(lines: list[str], ranges=False) -> str:
    aunts = parse_input(lines)
    for aunt in aunts:
        found = True
        for category in TICKER_TAPE:
            if aunts[aunt][category] != -1:
                if ranges:
                    if category in ["cats", "trees"]:
                        if aunts[aunt][category] <= TICKER_TAPE[category]:
                            found = False
                    elif category in ["pomeranians", "goldfish"]:
                        if aunts[aunt][category] >= TICKER_TAPE[category]:
                            found = False
                    else:
                        if TICKER_TAPE[category] != aunts[aunt][category]:
                            found = False
                else:
                    if TICKER_TAPE[category] != aunts[aunt][category]:
                        found = False
        if found:
            return aunt

    return ""


if __name__ == "__main__":
    print("The present is from aunt", solve(read_input_file("input.txt")))
    print("The present is from aunt", solve(read_input_file("input.txt"), True))
