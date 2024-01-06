import re
from itertools import product
from math import prod

from commons import read_input_file


def parse_input(lines: list[str]) -> list[list]:
    return [list(map(int, re.findall(r"-?\d+", line))) for line in lines]


def cockie_score(
    ingredients: list[list], distribution: tuple[int, ...]
) -> tuple[int, int]:
    score = [
        sum([factor * values[i] for factor, values in zip(distribution, ingredients)])
        for i in range(len(ingredients[0]))
    ]
    score = [s if s > 0 else 0 for s in score]
    return prod(score[:-1]), score[-1]


def solve(lines: list[str], calories: int = 0) -> int:
    ingredience = parse_input(lines)
    distributions = [
        d + (100 - sum(d),) for d in product(range(0, 101), repeat=len(ingredience) - 1)
    ]
    if calories > 0:
        cockie_scores = [cockie_score(ingredience, d) for d in distributions]
        cockie_scores = [c[0] for c in cockie_scores if c[1] == calories]
        return max(cockie_scores)
    else:
        return max([cockie_score(ingredience, d)[0] for d in distributions])


if __name__ == "__main__":
    print("The highest score is", solve(read_input_file("input.txt")))
    print(
        "The highest score with 500 calories is",
        solve(read_input_file("input.txt"), 500),
    )
