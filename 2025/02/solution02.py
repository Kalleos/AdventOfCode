from typing import Callable


def parse_input(filename: str):
    with open(filename) as file:
        line = file.readline().strip()
        ranges = line.split(",")
        ranges = [[int(n) for n in range.split("-")] for range in ranges]
        return ranges


def is_invalid(n):
    s = str(n)
    if len(s) % 2 != 0:
        return False
    half = len(s) // 2
    return s[0:half] == s[half:]


def is_invalid_2(n):
    s = str(n)
    m = len(s) // 2
    for i in range(1, m + 1):
        if len(s) % i == 0:
            ss = set([s[j:j + i] for j in range(0, len(s), i)])
            if len(ss) == 1:
                return True
    return False


def solve(filename: str, invalid_fn: Callable[[int], bool]):
    ranges = parse_input(filename)
    result = 0
    for start, end in ranges:
        for i in range(start, end + 1):
            if invalid_fn(i):
                result += i
    print(result)
    return result


if __name__ == '__main__':
    assert solve('test_input', is_invalid) == 1227775554
    assert solve('input', is_invalid) == 19574776074
    assert solve('test_input', is_invalid_2) == 4174379265
    assert solve('input', is_invalid_2) == 25912654282
