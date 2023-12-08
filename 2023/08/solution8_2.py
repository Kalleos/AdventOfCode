import itertools
import re
from math import lcm


def parse_instruction(line: str) -> tuple[str, tuple[str, str]]:
    m = re.findall(r'[A-Z0-9]+', line)
    return m[0], (m[1], m[2])


def solve(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()

        steps = lines[0]
        instructions = dict([parse_instruction(line) for line in lines[2:]])

        nodes = [k for k in instructions if k.endswith('A')]
        print(nodes)

        ns = []
        for start in nodes:
            node = start
            n = 0
            for step in itertools.cycle(steps):
                lr = 1 if step == 'R' else 0
                node = instructions[node][lr]
                n += 1
                if node.endswith('Z'):
                    break
            ns.append(n)
        print(ns)
        print(lcm(*ns))


if __name__ == '__main__':
    solve('test_input_2')
    solve('input')
