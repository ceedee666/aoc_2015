from commons import read_input_file


def parse_input(lines: list[str]) -> tuple[str, list[tuple[str, str]]]:
    replacements = [
        (line.split(" => ")[0], line.split(" => ")[1]) for line in lines[:-2]
    ]

    return lines[-1], replacements


def solve_part_1(lines: list[str]) -> int:
    molecules = set()
    molecule, replacements = parse_input(lines)
    for _str, replacement in replacements:
        idx = molecule.find(_str)
        while idx != -1:
            molecules.add(molecule[:idx] + replacement + molecule[idx + len(_str) :])
            idx = molecule.find(_str, idx + 1)
    return len(molecules)


def solve_part_2(lines: list[str]) -> int:
    molecule, replacements = parse_input(lines)

    reductions = {y: x for x, y in replacements}
    sorted_keys = sorted(reductions.keys(), key=lambda x: len(x), reverse=True)

    steps = 0
    while molecule != "e":
        for key in sorted_keys:
            if key in molecule:
                molecule = molecule.replace(key, reductions[key], 1)
                steps += 1
                break

    return steps


if __name__ == "__main__":
    print(
        solve_part_1(read_input_file("input.txt")),
        "different modules can be genearted.",
    )
    print(
        solve_part_2(read_input_file("input.txt")),
        "steps are needed to generate the molecule form e.",
    )
