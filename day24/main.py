from copy import deepcopy
from itertools import combinations
from math import prod

from commons import read_input_file


def solve(lines: list[str], groups: int = 3) -> int:
    weights = sorted([int(line) for line in lines])
    target_wight = sum(weights) // groups

    tmp_group = set()
    tmp_weights = deepcopy(weights)
    while sum(tmp_group) + tmp_weights[-1] < target_wight:
        tmp_group.add(tmp_weights.pop())

    min_group_len = len(tmp_group)

    found = False
    possible_groups = set()
    while not found:
        for group in combinations(weights, min_group_len):
            if sum(group) == target_wight:
                possible_groups.add(group)
                found = True

        min_group_len += 1

    return min([int(prod(g)) for g in possible_groups])


if __name__ == "__main__":
    print(
        "The quantum entanglement of the first group of packages is:",
        solve(read_input_file("input.txt")),
    )
    print(
        "The quantum entanglement of the first group of packages is:",
        solve(read_input_file("input.txt"), 4),
    )
