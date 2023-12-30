from commons import read_input_file

DIRS = {
    "<": complex(-1, 0),
    ">": complex(1, 0),
    "^": complex(0, -1),
    "v": complex(0, 1),
}


def solve_part_1(filename: str):
    commands = read_input_file(filename)[0]
    visited = set()

    pos = complex(0, 0)
    visited.add(pos)
    for c in commands:
        pos += DIRS[c]
        visited.add(pos)

    return len(visited)


def solve_part_2(filename: str):
    commands = read_input_file(filename)[0]
    visited = set()

    pos_santa = complex(0, 0)
    pos_robot_santa = complex(0, 0)
    visited.add(pos_santa)

    for c_stata, c_robot_santa in zip(*[iter(commands)] * 2):
        pos_santa += DIRS[c_stata]
        pos_robot_santa += DIRS[c_robot_santa]
        visited.add(pos_santa)
        visited.add(pos_robot_santa)

    return len(visited)


if __name__ == "__main__":
    print(solve_part_1("input.txt"), "houses receive at least one present.")
    print(solve_part_2("input.txt"), "houses receive at least one present.")
