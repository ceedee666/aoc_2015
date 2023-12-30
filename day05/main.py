import re
import string
from collections import Counter

from commons import read_input_file


def no_ab_cd_pq_xy(line: str) -> bool:
    return not ("ab" in line or "cd" in line or "pq" in line or "xy" in line)


def at_least_one_letter_twice(line: str) -> bool:
    return any(c * 2 in line for c in string.ascii_lowercase)


def contains_3_vowels(line: str) -> bool:
    count = Counter(line)
    return sum(count[c] for c in "aieou") >= 3


def is_nice_part_1(line: str) -> bool:
    return all(
        (
            contains_3_vowels(line),
            at_least_one_letter_twice(line),
            no_ab_cd_pq_xy(line),
        )
    )


def is_nice_part_2(line: str) -> bool:
    regex_1 = r"([a-z]{2}).*?\1"
    regex_2 = r"([a-z]).\1"

    return re.search(regex_1, line) and re.search(regex_2, line)


def solve_part_1(filename: str) -> int:
    return sum(1 for line in read_input_file(filename) if is_nice_part_1(line))


def solve_part_2(filename: str) -> int:
    return sum(1 for line in read_input_file(filename) if is_nice_part_2(line))


if __name__ == "__main__":
    print(solve_part_1("input.txt"), "strings are nice.")
    print(solve_part_2("input.txt"), "strings are nice.")
