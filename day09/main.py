from itertools import permutations

from commons import read_input_file


def parse_input(lines: list[str]) -> tuple[set, dict]:
    distances = {}
    cities = set()
    for line in lines:
        parts = line.split(" ")
        distances[(parts[0], parts[2])] = int(parts[-1])
        distances[(parts[2], parts[0])] = int(parts[-1])
        cities.add(parts[0])
        cities.add(parts[2])
    return cities, distances


def path_length(path: tuple, distances: dict) -> int:
    return sum([distances[p] for p in zip(path, path[1:])])


def solve(filename: str) -> tuple[int, int]:
    lines = read_input_file(filename)
    cities, distances = parse_input(lines)
    path_lengths = [path_length(p, distances) for p in permutations(cities)]
    return min(path_lengths), max(path_lengths)


if __name__ == "__main__":
    print("The distance of the shortest route is", solve("input.txt")[0])
    print("The distance of the longest route is", solve("input.txt")[1])
