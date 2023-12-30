import re
from collections import defaultdict
from enum import Enum

from commons import read_input_file


class Operation(Enum):
    ON = 1
    OFF = 2
    TOGGLE = 3


def parse_operation(line: str) -> Operation:
    if "turn on" in line:
        return Operation.ON
    elif "turn off" in line:
        return Operation.OFF
    else:
        return Operation.TOGGLE


def parse_input(lines: list[str]) -> list:
    return [
        ([int(n) for n in re.findall(r"\d+", line)], parse_operation(line))
        for line in lines
    ]


def solve(filename: str, part_1: bool = True) -> int:
    instructions = parse_input(read_input_file(filename))
    lights = defaultdict(int)

    for (row_start, col_start, row_end, col_end), operation in instructions:
        for row in range(row_start, row_end + 1):
            for col in range(col_start, col_end + 1):
                match operation:
                    case Operation.ON:
                        if part_1:
                            lights[(row, col)] = 1
                        else:
                            lights[(row, col)] += 1
                    case Operation.OFF:
                        lights[(row, col)] = max(0, lights[(row, col)] - 1)
                    case Operation.TOGGLE:
                        if part_1:
                            lights[(row, col)] ^= 1
                        else:
                            lights[(row, col)] += 2

    return sum(lights.values())


if __name__ == "__main__":
    print(solve("input.txt"), "lights are on.")
    print("The total brightness is", solve("input.txt", False))
