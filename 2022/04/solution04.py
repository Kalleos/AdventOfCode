def parse_pairs(line: str):
    return [[int(n) for n in section.split('-')] for section in line.split(',')]


def fully_contains(pairs):
    return pairs[0][0] <= pairs[1][0] and pairs[1][1] <= pairs[0][1] or pairs[1][0] <= pairs[0][0] and pairs[0][1] <= \
        pairs[1][1]


def overlaps(pairs):
    return pairs[0][0] <= pairs[1][0] <= pairs[0][1] or pairs[1][0] <= pairs[0][0] <= pairs[1][1]


def solve(filename):
    with (open(filename) as file):
        lines = file.read().splitlines()
        cnt = sum([1 for line in lines if fully_contains(parse_pairs(line))])
        print('fully_contains', cnt)
        cnt = sum([1 for line in lines if overlaps(parse_pairs(line))])
        print('overlaps', cnt)


if __name__ == '__main__':
    solve('test_input')
    solve('input')
