from itertools import chain, combinations

from commons import read_input_file


def powerset(numbers: list[int]) -> list[tuple[int, ...]]:
    return list(
        chain.from_iterable(
            combinations(numbers, r) for r in range(1, len(numbers) + 1)
        )
    )


def solve(lines: list[str], min_lenght=False) -> int:
    numbers = [int(line) for line in lines]
    power_set = powerset(numbers)
    possible_combinations = [s for s in power_set if sum(s) == 150]
    if min_lenght:
        min_len = min([len(c) for c in possible_combinations])
        possible_combinations = [c for c in possible_combinations if len(c) == min_len]
    return len(possible_combinations)


if __name__ == "__main__":
    print(
        "The are",
        solve(read_input_file("input.txt")),
        "different combinations of containers.",
    )
    print(
        "The are",
        solve(read_input_file("input.txt"), True),
        "different combinations of containers.",
    )
