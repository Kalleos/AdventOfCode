def get_priority(c):
    ord_c = ord(c)
    if 65 <= ord_c <= 90:
        return ord_c - 38
    if 97 <= ord_c <= 122:
        return ord_c - 96
    raise ValueError('Something went wrong')


def get_same_char(s1, s2):
    return [c for c in s1 if c in s2][0]


def solve(filename):
    with (open(filename) as file):
        lines = file.read().splitlines()
        print(sum([get_priority(get_same_char(line[0:len(line) // 2], line[len(line) // 2:])) for line in lines]))


if __name__ == '__main__':
    solve('test_input')
    solve('input')
