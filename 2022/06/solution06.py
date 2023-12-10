from itertools import groupby


def are_all_different(four_chars: str):
    return len([g for g in groupby(sorted(four_chars))]) == len(four_chars)


def find_marker(line, l):
    for k in range(len(line) - l):
        if are_all_different(line[k:k + l]):
            print(k + l)
            break


def solve(filename):
    with (open(filename) as file):
        lines = file.read().splitlines()
        for line in lines:
            find_marker(line, 4)
            find_marker(line, 14)


if __name__ == '__main__':
    solve('test_input')
    solve('input')
