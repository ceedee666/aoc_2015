from copy import copy
from dataclasses import dataclass, field
from enum import Enum

from commons import read_input_file


class Operation(Enum):
    NONE = 0
    VALUE = 1
    AND = 2
    OR = 3
    NOT = 4
    LSHIFT = 5
    RSHIFT = 6


@dataclass(frozen=True)
class LogicGate:
    output: str
    operation: Operation
    inputs: dict[int, str] = field(default_factory=dict)
    values: dict[int, int] = field(default_factory=dict)

    def is_active(self, wire_values: dict[str, int]) -> bool:
        return self.operation == Operation.VALUE or all(
            [self.inputs[pos] in wire_values for pos in self.inputs]
        )

    def __value_at_pos(self, pos: int, wire_values: dict[str, int]) -> int:
        return wire_values[self.inputs[pos]] if pos in self.inputs else self.values[pos]

    def output_value(self, wire_values: dict[str, int]) -> int:
        match self.operation:
            case Operation.VALUE:
                result = self.values[0]
            case Operation.NONE:
                result = wire_values[self.inputs[0]]
            case Operation.NOT:
                if self.values:
                    result = ~self.values[0]
                else:
                    result = ~wire_values[self.inputs[0]]
            case Operation.AND:
                a = self.__value_at_pos(0, wire_values)
                b = self.__value_at_pos(1, wire_values)
                result = a & b
            case Operation.OR:
                a = self.__value_at_pos(0, wire_values)
                b = self.__value_at_pos(1, wire_values)
                result = a | b
            case Operation.LSHIFT:
                a = self.__value_at_pos(0, wire_values)
                result = a << self.values[1]
            case Operation.RSHIFT:
                a = wire_values[self.inputs[0]] if 0 in self.inputs else self.values[0]
                result = a >> self.values[1]
            case _:
                raise NotImplementedError
        return result


def parse_gate(line: str) -> LogicGate:
    values, inputs = {}, {}

    input, output = line.split(" -> ")

    if input.isdecimal():
        op = "VALUE"
        values = {0: int(input)}

    elif " " not in input:
        op = "NONE"
        inputs = {0: input}

    elif "NOT" in input:
        op, a = input.split()
        if a.isdecimal():
            values = {0: int(a)}
        else:
            inputs = {0: a}
    else:
        a, op, b = input.split()

        if a.isdecimal():
            values[0] = int(a)
        else:
            inputs[0] = a
        if b.isdecimal():
            values[1] = int(b)
        else:
            inputs[1] = b

    return LogicGate(output, Operation[op], values=values, inputs=inputs)


def execute(all_gates: list[LogicGate]) -> dict[str, int]:
    wire_values = {}

    visited_gates = []
    active_gates = [gate for gate in all_gates if gate.is_active(wire_values)]
    all_gates = [gate for gate in all_gates if gate not in active_gates]

    while active_gates:
        for gate in active_gates:
            wire_values[gate.output] = gate.output_value(wire_values)
        visited_gates.extend(active_gates)
        active_gates = [gate for gate in all_gates if gate.is_active(wire_values)]
        all_gates = [gate for gate in all_gates if gate not in active_gates]

    return wire_values


def parse_input(lines: list[str]) -> list[LogicGate]:
    return [parse_gate(line) for line in lines]


def solve_part_1(lines: list[str]) -> int:
    all_gates = parse_input(lines)
    wire_values = execute(all_gates)
    return wire_values["a"]


def solve_part_2(lines: list[str]) -> int:
    gates = parse_input(lines)

    all_gates = copy(gates)
    wire_values = execute(all_gates)
    new_b_value = wire_values["a"]

    all_gates = copy(gates)
    all_gates = [
        gate
        for gate in gates
        if not (gate.output == "b" and gate.operation == Operation.VALUE)
    ]
    all_gates.append(LogicGate("b", Operation.VALUE, values={0: new_b_value}))
    wire_values = execute(all_gates)
    return wire_values["a"]


if __name__ == "__main__":
    print("The signal at wire a is", solve_part_1(read_input_file("input.txt")))
    print("The signal at wire a is", solve_part_2(read_input_file("input.txt")))
