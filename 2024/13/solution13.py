import re


class Machine:

    def __init__(self, x, y, x_a, y_a, x_b, y_b):
        self.x = x
        self.y = y
        self.x_a = x_a
        self.y_a = y_a
        self.x_b = x_b
        self.y_b = y_b


pattern_button_a = re.compile("Button A: X\+(\d+), Y\+(\d+)")
pattern_button_b = re.compile("Button B: X\+(\d+), Y\+(\d+)")
pattern_prize = re.compile("Prize: X=(\d+), Y=(\d+)")


def solve(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()
        machines = []
        for line in lines:
            if m := pattern_button_a.match(line):
                x_a = int(m.group(1))
                y_a = int(m.group(2))
            if m := pattern_button_b.match(line):
                x_b = int(m.group(1))
                y_b = int(m.group(2))
            if m := pattern_prize.match(line):
                x = int(m.group(1))
                y = int(m.group(2))
                machines.append(Machine(x, y, x_a, y_a, x_b, y_b))

        calc_tokens(machines)
        for ma in machines:
            ma.x = ma.x + 10000000000000
            ma.y = ma.y + 10000000000000
        calc_tokens(machines)


def calc_tokens(machines):
    tokens = 0
    for ma in machines:
        a = (ma.x_b * ma.y - ma.y_b * ma.x) / (ma.y_a * ma.x_b - ma.x_a * ma.y_b)
        b = (ma.x - ma.x_a * a) / ma.x_b
        if int(a) == a and int(b) == b:
            tokens += 3 * a + b
    print(tokens)


if __name__ == '__main__':
    solve('test_input')  # 480, 875318608908
    solve('input')  # 35082, 82570698600470
