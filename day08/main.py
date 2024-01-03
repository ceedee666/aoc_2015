from commons import read_input_file


def solve_part_1(filename: str) -> int:
    strings = read_input_file(filename)
    code_lenght = [len(s) for s in strings]
    char_lenght = [len(eval(s)) for s in strings]
    return sum(code_lenght) - sum(char_lenght)


def solve_part_2(filename: str) -> int:
    strings = read_input_file(filename)
    code_lenght = [len(s) for s in strings]
    encoded_strings = [
        '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"' for s in strings
    ]
    encoded_lenght = [len(s) for s in encoded_strings]
    return sum(encoded_lenght) - sum(code_lenght)


if __name__ == "__main__":
    print("The value for part 1 is", solve_part_1("input.txt"))
    print("The value for part 2 is", solve_part_2("input.txt"))
