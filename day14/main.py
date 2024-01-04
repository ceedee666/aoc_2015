import re
from collections import defaultdict

from commons import read_input_file


def parse_input(lines: list[str]) -> dict[str, tuple[int, ...]]:
    return {
        line.split(" ")[0]: tuple(map(int, re.findall(r"\d+", line))) for line in lines
    }


def traveled_distance(speed: int, fly_time: int, rest_time: int, time: int) -> int:
    cycle = fly_time + rest_time
    cycles, reminder = divmod(time, cycle)
    return speed * cycles * fly_time + min(fly_time, reminder) * speed


def solve_part_1(filename: str, time: int = 2503) -> int:
    lines = read_input_file(filename)
    reindeers = parse_input(lines)
    return max(
        [
            traveled_distance(speed, fly_time, rest_time, time)
            for _, (speed, fly_time, rest_time) in reindeers.items()
        ]
    )


def solve_part_2(filename: str, time: int = 2503) -> int:
    lines = read_input_file(filename)
    reindeers = parse_input(lines)

    points = defaultdict(int)
    for t in range(1, time + 1):
        distances = {
            reindeer: traveled_distance(speed, fly_time, rest_time, t)
            for reindeer, (speed, fly_time, rest_time) in reindeers.items()
        }
        leaders = [
            reindeer
            for reindeer in distances
            if distances[reindeer] == max(distances.values())
        ]

        for leader in leaders:
            points[leader] += 1

    return max(points.values())


if __name__ == "__main__":
    print("The winning reindeer traveled", solve_part_1("input.txt"), "km.")
    print("The winning reindeer has", solve_part_2("input.txt"), "points.")
