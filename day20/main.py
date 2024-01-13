import math


def generate_divisors(n: int):
    small_divisors = [i for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0]
    large_divisors = [n / d for d in small_divisors if n != d * d]
    return small_divisors + large_divisors


def solve_part_1(value: int) -> int:
    for i in range(1, int(value / 10)):
        parcels = sum(generate_divisors(i))
        if parcels >= value / 10:
            return i
    return 0


def solve_part_2(value: int) -> int:
    for i in range(1, int(value / 11)):
        parcels = sum([d for d in generate_divisors(i) if i / d < 50])
        if parcels >= value / 11:
            return i
    return 0


if __name__ == "__main__":
    print("The lowest house number is:", solve_part_1(33100000))
    print("The lowest house number is:", solve_part_2(33100000))
