def get_priority(c):
    ord_c = ord(c)
    if 65 <= ord_c <= 90:
        return ord_c - 38
    if 97 <= ord_c <= 122:
        return ord_c - 96
    raise ValueError('Something went wrong')


def get_common_char(s1, s2, s3):
    return [c for c in s1 if c in s2 and c in s3][0]


def solve(filename):
    with (open(filename) as file):
        lines = file.read().splitlines()
        result = 0
        for i in range(len(lines) // 3):
            result += get_priority(get_common_char(lines[3 * i], lines[3 * i + 1], lines[3 * i + 2]))

        print(result)


if __name__ == '__main__':
    solve('test_input')
    solve('input')
