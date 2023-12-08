import itertools
import re


def parse_instruction(line: str):
    m = re.findall(r'[A-Z]+', line)
    return (m[0], (m[1], m[2]))


def solve(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()

        steps = lines[0]
        instructions = dict([parse_instruction(line) for line in lines[2:]])

        node = 'AAA'
        end = 'ZZZ'

        n = 0
        for step in itertools.cycle(steps):
            lr = 1 if step == 'R' else 0
            node = instructions[node][lr]
            n += 1
            if node == end:
                break

        print(n)


if __name__ == '__main__':
    solve('test_input')
    solve('input')
