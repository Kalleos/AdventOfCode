import itertools

from attr import dataclass


@dataclass
class Gate:
    operator: str  # "AND" | "OR" | "XOR"
    input1: str
    input2: str
    output: str


def parse_input(filename: str):
    with open(filename) as file:
        blocks = file.read().split("\n\n")
        wires = {key: int(value) for key, value in [line.split(": ") for line in blocks[0].splitlines()]}
        gates = [Gate(splitted[1], splitted[0], splitted[2], splitted[4]) for splitted in
                 [line.split(" ") for line in blocks[1].splitlines()]]

        return wires, gates


def operate(wires, gates):
    for gate in gates:
        if gate.input1 in wires and gate.input2 in wires:
            if gate.operator == "AND":
                wires[gate.output] = wires[gate.input1] & wires[gate.input2]
            elif gate.operator == "OR":
                wires[gate.output] = wires[gate.input1] | wires[gate.input2]
            elif gate.operator == "XOR":
                wires[gate.output] = wires[gate.input1] ^ wires[gate.input2]


def get_number(wires):
    result = 0
    for key, value in wires.items():
        if key.startswith("z"):
            result += value << int(key[1:])
    return result


def get_output(wires, gates):
    old_len = 0
    while len(wires) != old_len:
        old_len = len(wires)
        operate(wires, gates)
    return get_number(wires)


def set_input(x, y):
    wires = {}
    for i in range(45):
        wires[f"x{str(i).rjust(2, '0')}"] = (x >> i) & 1
        wires[f"y{str(i).rjust(2, '0')}"] = (y >> i) & 1
    return wires


def swap(gates, i, j):
    temp = gates[i].output
    gates[i].output = gates[j].output
    gates[j].output = temp


def solve_part1(filename: str):
    wires, gates = parse_input(filename)
    print(get_output(wires, gates))


def draw_gates(gates):
    with open("gates.mermaid", "w") as f:
        f.write("graph TD;\n")
        for gate in gates:
            f.write(f"{gate.input1} -->|{gate.operator}| {gate.output};\n")
            f.write(f"{gate.input2} -->|{gate.operator}| {gate.output};\n")


def gate_id(gates: list[Gate], name: str):
    for i, gate in enumerate(gates):
        if gate.output == name:
            return i


def solve_part2(filename: str):
    _, gates = parse_input(filename)
    draw_gates(gates)

    for gate in gates:
        if gate.operator == "OR" and gate.output.startswith("z"):
            print(gate)
        if gate.operator == "AND" and gate.output.startswith("z"):
            print(gate)

    inputs = [(35184372088831, 35184372088831), (345345, 534345), (0, 0), (1, 1), (35184372088831, 1)]

    swap(gates, gate_id(gates, "z07"), gate_id(gates, "nqk"))
    swap(gates, gate_id(gates, "z24"), gate_id(gates, "fpq"))
    swap(gates, gate_id(gates, "z32"), gate_id(gates, "srn"))
    for perm in itertools.permutations(range(len(gates)), 2):
        if perm[0] < perm[1]:
            swap(gates, perm[0], perm[1])
            all_equals = True
            for (x, y) in inputs:
                wires = set_input(x, y)
                if get_output(wires, gates) != x + y:
                    all_equals = False
                    break
            swap(gates, perm[0], perm[1])
            if all_equals:
                print(gates[perm[0]], gates[perm[1]])


if __name__ == '__main__':
    solve_part1('test_input')
    solve_part1('test_input2')
    solve_part1('input')

    solve_part2('input')
