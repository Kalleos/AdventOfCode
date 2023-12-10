import copy
import re


def parse_stacks(lines: list[str]):
    n = len(lines[-1]) // 4 + 1
    stacks = [[] for _ in range(n)]
    for row in reversed(lines):
        for k in range(len(row) // 4 + 1):
            crate = row[4 * k + 1]
            if crate != ' ':
                stacks[k].append(crate)
    return stacks


def parse_moves(lines: list[str]):
    r = re.compile(r'move (\d+) from (\d+) to (\d+)')
    moves = []
    for line in lines:
        m = r.match(line)
        move = [int(m[k]) for k in range(1, 4)]
        moves.append(move)
    return moves


def rearrange_stacks(stacks: list[list[str]], moves):
    new_stack = copy.deepcopy(stacks)
    for move in moves:
        for _ in range(move[0]):
            new_stack[move[2] - 1].append(new_stack[move[1] - 1].pop())
    return new_stack


def rearrange_stacks_9001(stacks: list[list[str]], moves):
    new_stack = copy.deepcopy(stacks)
    for move in moves:
        new_stack[move[2] - 1].extend(new_stack[move[1] - 1][-move[0]:])
        new_stack[move[1] - 1] = new_stack[move[1] - 1][0:-move[0]]
    return new_stack


def solve(filename):
    with (open(filename) as file):
        lines = file.read().splitlines()
        empty_line = lines.index('')
        stacks = parse_stacks(lines[0:empty_line - 1])
        print(stacks)
        moves = parse_moves(lines[empty_line + 1:])
        # print(moves)
        stacks_9000 = rearrange_stacks(stacks, moves)
        print(stacks_9000)
        print('result 1#', ''.join([stack[-1] for stack in stacks_9000]))

        stacks_9001 = rearrange_stacks_9001(stacks, moves)
        print(stacks_9001)
        print('result 2#', ''.join([stack[-1] for stack in stacks_9001]))


if __name__ == '__main__':
    solve('test_input')
    solve('input')
