from functools import cache

NUMERIC_KEYPAD = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
    '_': (3, 0), '0': (3, 1), 'A': (3, 2),
}

DIRECTIONAL_KEYPAD = {
    '_': (0, 0), '^': (0, 1), 'A': (0, 2),
    '<': (1, 0), 'v': (1, 1), '>': (1, 2),
}


def parse_input(filename: str) -> list[str]:
    with open(filename) as file:
        return file.read().splitlines()


def get_sequences(start: str, end: str, keypad: dict[str, tuple[int, int]]) -> list[str]:
    start = keypad[start]
    end = keypad[end]
    gap = keypad['_']

    vertical = ""
    if start[0] < end[0]:
        vertical = "v" * (end[0] - start[0])
    if start[0] > end[0]:
        vertical = "^" * (start[0] - end[0])

    horizontal = ""
    if start[1] < end[1]:
        horizontal = ">" * (end[1] - start[1])
    if start[1] > end[1]:
        horizontal = "<" * (start[1] - end[1])

    if vertical == "":
        return [horizontal]
    if horizontal == "":
        return [vertical]
    if start[0] == gap[0] and end[1] == gap[1]:
        return [vertical + horizontal]
    if start[1] == gap[1] and end[0] == gap[0]:
        return [horizontal + vertical]
    return [vertical + horizontal, horizontal + vertical]


def shortest_length_numeric(start, end, n):
    codes = [code + 'A' for code in get_sequences(start, end, NUMERIC_KEYPAD)]
    return min([shortest_length_directional(code, n) for code in codes])


@cache
def shortest_length_directional(code, n):
    if n == 0:
        return len(code)
    length = 0
    old_c = 'A'
    for c in code:
        length += min(
            [shortest_length_directional(seq + 'A', n - 1) for seq in get_sequences(old_c, c, DIRECTIONAL_KEYPAD)])
        old_c = c
    return length


def solve(filename: str, n: int):
    result = 0
    codes = parse_input(filename)
    for code in codes:
        length = 0
        old_c = 'A'
        for c in code:
            length += shortest_length_numeric(old_c, c, n)
            old_c = c
        result += length * int(code[:3])

    print(result)


if __name__ == '__main__':
    solve('test_input', 2)
    solve('input', 2)
    solve('test_input', 25)
    solve('input', 25)
