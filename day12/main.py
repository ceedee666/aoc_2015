import json
import re

from commons import read_input_file


def solve_part_1(filename: str) -> int:
    lines = read_input_file(filename)
    return sum([int(x) for x in re.findall(r"-?\d+", lines[0])])


def sum_json_values(data) -> int:
    match data:
        case int():
            return data
        case dict():
            if "red" in data.values():
                return 0
            else:
                return sum(sum_json_values(x) for x in data.values())
        case list():
            return sum(sum_json_values(x) for x in data)
        case _:
            return 0


def solve_part_2(filename: str) -> int:
    data = json.loads(read_input_file(filename)[0])
    return sum_json_values(data)


if __name__ == "__main__":
    print("The sum of all numbers is", solve_part_1("input.txt"))
    print("The sum of all numbers w/o anything red is", solve_part_2("input.txt"))
