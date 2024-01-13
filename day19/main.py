from commons import read_input_file


def parse_input(lines: list[str]) -> tuple[str, list[tuple[str, str]]]:
    replacements = [
        (line.split(" => ")[0], line.split(" => ")[1]) for line in lines[:-2]
    ]

    return lines[-1], replacements


def solve(lines: list[str]) -> int:
    molecules = set()
    molecule, replacements = parse_input(lines)
    for _str, replacement in replacements:
        idx = molecule.find(_str)
        while idx != -1:
            molecules.add(molecule[:idx] + replacement + molecule[idx + len(_str) :])
            idx = molecule.find(_str, idx + 1)
    return len(molecules)


if __name__ == "__main__":
    print(solve(read_input_file("input.txt")), "different modules can be genearted.")
