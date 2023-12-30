import hashlib
from itertools import count

INPUT = "ckczppom"


def solve_part_1():
    for i in count(1):
        if hashlib.md5(f"{INPUT}{i}".encode()).hexdigest().startswith("00000"):
            return i


def solve_part_2():
    for i in count(1):
        if hashlib.md5(f"{INPUT}{i}".encode()).hexdigest().startswith("000000"):
            return i


if __name__ == "__main__":
    print(
        solve_part_1(), "is the lowest number for which the MD5 hash starts with 00000."
    )

    print(
        solve_part_2(),
        "is the lowest number for which the MD5 hash starts with 000000.",
    )
