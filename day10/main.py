from itertools import groupby


def solve(sequence: str, iterations: int = 40) -> int:
    for _ in range(iterations):
        grouped = groupby(sequence)
        sequence = "".join(f"{len(list(v))}{k}" for k, v in grouped)
    return len(sequence)


if __name__ == "__main__":
    print("The lenght of the result is", solve("3113322113"))
    print("The lenght of the result is", solve("3113322113", 50))
