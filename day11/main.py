import re
import string
from functools import reduce


def increment(passwd: str) -> str:
    for i in range(len(passwd) - 1, -1, -1):
        if passwd[i] == "z":
            passwd = passwd[:i] + "a" + passwd[i + 1 :]
        else:
            passwd = passwd[:i] + chr(ord(passwd[i]) + 1) + passwd[i + 1 :]
            break
    return passwd


def check_is_valid(passwd: str) -> bool:
    no_iol = all(c not in passwd for c in "iol")

    repeating_chars = re.findall(r"([a-z])\1", passwd)
    if len(repeating_chars) >= 2:
        two_pairs = reduce(lambda x, y: x != y, repeating_chars)
    else:
        two_pairs = False

    increasing_straight = any(
        [
            "".join(seq) in passwd
            for seq in zip(
                string.ascii_lowercase,
                string.ascii_lowercase[1:],
                string.ascii_lowercase[2:],
            )
        ]
    )

    return no_iol and two_pairs and increasing_straight


def solve(passwd: str) -> str:
    is_valid = False
    while not is_valid:
        passwd = increment(passwd)
        is_valid = check_is_valid(passwd)
    return passwd


if __name__ == "__main__":
    print("The next password should be", solve("vzbxkghb"))
    print("The next password should be", solve("vzbxxyzz"))
