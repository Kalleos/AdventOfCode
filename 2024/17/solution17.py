import re


def parse_input(filename: str):
    register = []
    program = []
    with open(filename) as file:
        lines = file.read().splitlines()
        pattern_register = re.compile("Register [ABC]: (\d+)")
        pattern_program = re.compile("Program: ([\d,]+)")
        for line in lines:
            if match := pattern_register.match(line):
                register.append(int(match.group(1)))
            if match := pattern_program.match(line):
                program = list(map(int, match.group(1).split(",")))
    return register, program


def get_combo_operand(operand, register):
    if operand in [0, 1, 2, 3]:
        return operand
    if operand in [4, 5, 6]:
        return register[operand - 4]
    raise ValueError


def operate(instructions, register):
    output = []
    ip = 0
    while ip < len(instructions):
        (opcode, operand) = instructions[ip], instructions[ip + 1]
        if opcode == 0:
            register[0] = register[0] >> get_combo_operand(operand, register)
            ip += 2
        if opcode == 1:
            register[1] = register[1] ^ operand
            ip += 2
        if opcode == 2:
            register[1] = get_combo_operand(operand, register) % 8
            ip += 2
        if opcode == 3:
            if register[0] != 0:
                ip = operand
            else:
                ip += 2
        if opcode == 4:
            register[1] = register[1] ^ register[2]
            ip += 2
        if opcode == 5:
            output.append(get_combo_operand(operand, register) % 8)
            ip += 2
        if opcode == 6:
            register[1] = register[0] >> get_combo_operand(operand, register)
            ip += 2
        if opcode == 7:
            register[2] = register[0] >> get_combo_operand(operand, register)
            ip += 2
    return register, output


def solve(filename: str):
    register, program = parse_input(filename)
    _, output = operate(program, register)
    print(",".join(map(str, output)))

    inputs = [0]
    for n in range(1, 17):
        next_inputs = []
        for input in inputs:
            for i in range(input << 3, (input + 1) << 3):
                _, output = operate(program, [i, 0, 0])
                if program[-n:] == output:
                    next_inputs.append(i)
        inputs = next_inputs
    if inputs:
        print(inputs[0])


if __name__ == '__main__':
    assert operate([2, 6], [0, 0, 9]) == ([0, 1, 9], [])
    assert operate([5, 0, 5, 1, 5, 4], [10, 0, 0]) == ([10, 0, 0], [0, 1, 2])
    assert operate([0, 1, 5, 4, 3, 0], [2024, 0, 0]) == ([0, 0, 0], [4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0])
    solve('test_input')
    solve('input')
