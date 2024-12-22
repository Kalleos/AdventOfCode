def parse_input(filename: str):
    with open(filename) as file:
        blocks = file.read().split('\n\n')
        towel_patterns = blocks[0].split(', ')
        designs = blocks[1].splitlines()
        return towel_patterns, designs


def is_possible(towel_patterns: list[str], design: str):
    if design in towel_patterns:
        return True
    for pattern in towel_patterns:
        if design.startswith(pattern):
            if is_possible(towel_patterns, design[len(pattern):]):
                return True
    return False


possible_ways = {}


def cnt_possible_ways(towel_patterns: list[str], design: str):
    if design in possible_ways:
        return possible_ways[design]
    if len(design) == 0:
        return 1
    cnt = 0
    for pattern in towel_patterns:
        if design.startswith(pattern):
            ways = cnt_possible_ways(towel_patterns, design[len(pattern):])
            cnt += ways
    possible_ways[design] = cnt
    return cnt


def solve(filename: str):
    towel_patterns, designs = parse_input(filename)

    cnt = 0
    for design in designs:
        if is_possible(towel_patterns, design):
            cnt += 1
    print(cnt)

    possible_ways.clear()
    cnt = 0
    for design in designs:
        ways = cnt_possible_ways(towel_patterns, design)
        cnt += ways
    print(cnt)


if __name__ == '__main__':
    solve('test_input')
    solve('input')
