from commons import read_input_file


def parse_grid(lines: list[str]) -> list[list[bool]]:
    return [[True if c == "#" else False for c in line] for line in lines]


def initialize_grid(rows: int, cols: int) -> list[list[bool]]:
    return [[False for _ in range(cols)] for _ in range(rows)]


def neighbours(row: int, col: int, grid: list[list[bool]]) -> list[bool]:
    neighbours = []
    for d_row in (-1, 0, 1):
        for d_col in (-1, 0, 1):
            if (
                row + d_row >= 0
                and row + d_row < len(grid[0])
                and col + d_col >= 0
                and col + d_col < len(grid)
            ):
                if d_row != 0 or d_col != 0:
                    neighbours.append(grid[row + d_row][col + d_col])
    return neighbours


def next_state(grid: list[list[bool]], corners_on: bool) -> list[list[bool]]:
    new_grid = initialize_grid(len(grid), len(grid[0]))
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            active_neighbours = sum(neighbours(row, col, grid))
            if grid[row][col] and active_neighbours in [2, 3]:
                new_grid[row][col] = True
            if not grid[row][col] and active_neighbours == 3:
                new_grid[row][col] = True

    if corners_on:
        for row in [0, -1]:
            for col in [0, -1]:
                new_grid[row][col] = True
    return new_grid


def solve(lines: list[str], steps: int = 100, corners_on: bool = False) -> int:
    grid = parse_grid(lines)
    for _ in range(steps):
        grid = next_state(grid, corners_on)
    return sum(sum(row) for row in grid)


if __name__ == "__main__":
    print("After 100 steps", solve(read_input_file("input.txt")), "lights are on.")
    print(
        "After 100 steps",
        solve(read_input_file("input.txt"), corners_on=True),
        "lights are on.",
    )
