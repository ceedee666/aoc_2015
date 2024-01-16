def solve(start_value: int, row: int, col: int) -> int:
    #    | 1   2   3   4   5   6
    # ---+---+---+---+---+---+---+
    #  1 |  1   3   6  10  15  21
    #  2 |  2   5   9  14  20
    #  3 |  4   8  13  19
    #  4 |  7  12  18
    #  5 | 11  17
    #  6 | 16

    # We need to calculate the trianlge numbers
    value = start_value
    x = row - 1 + col - 1
    sum_x = x * (x + 1) // 2
    for _ in range(sum_x + col - 1):
        value = (value * 252533) % 33554393
    return value


if __name__ == "__main__":
    start_value = 20151125
    row, col = 2981, 3075
    print("The code for the machine is", solve(start_value, row, col))
