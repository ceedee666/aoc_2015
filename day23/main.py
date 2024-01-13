from collections import defaultdict

from commons import read_input_file


def parse_params(param: str) -> tuple[str, int]:
    if ", " in param:
        return (param[0], int(param[2:]))
    elif param[0] in "+-":
        return ("", int(param))
    else:
        return (param, 0)


def parse_instructions(lines: list[str]) -> list[tuple[str, str, int]]:
    instructions = [(line[:3], line[4:]) for line in lines]
    return [(inst,) + parse_params(param) for inst, param in instructions]


def execute_instructions(
    instructions: list[tuple[str, str, int]], a: int
) -> dict[str, int]:
    register = defaultdict(int)
    register["a"] = a
    inst_pointer = 0
    while inst_pointer < len(instructions):
        inst, param, value = instructions[inst_pointer]
        match inst:
            case "hlf":
                register[param] = register[param] // 2
                inst_pointer += 1
            case "tpl":
                register[param] *= 3
                inst_pointer += 1
            case "inc":
                register[param] += 1
                inst_pointer += 1
            case "jmp":
                inst_pointer += value
            case "jie":
                if register[param] % 2 == 0:
                    inst_pointer += value
                else:
                    inst_pointer += 1
            case "jio":
                if register[param] == 1:
                    inst_pointer += value
                else:
                    inst_pointer += 1

    return register


def solve(lines: list[str], a: int = 0) -> int:
    instructions = parse_instructions(lines)
    registers = execute_instructions(instructions, a=a)
    return registers["b"]


if __name__ == "__main__":
    print("The value in register b is:", solve(read_input_file("input.txt")))
    print("The value in register b is:", solve(read_input_file("input.txt"), 1))
