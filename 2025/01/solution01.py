def parse_input(filename: str):
    with open(filename) as file:
        rotation_raw = [line.strip() for line in file.readlines()]
        return [(rot[0], int(rot[1:])) for rot in rotation_raw]


def part1(filename: str):
    rotations = parse_input(filename)
    dial = 50
    result = 0
    for (direction, dist) in rotations:
        if direction == 'R':
            dial = (dial + dist) % 100
        if direction == 'L':
            dial = (dial - dist) % 100
        if dial == 0:
            result += 1
    print(result)
    return result


def part2(filename: str):
    rotations = parse_input(filename)
    dial = 50
    result = 0
    for (direction, dist) in rotations:
        if direction == 'R':
            step1 = dial + dist
            result += int(step1 / 100)
            dial = step1 % 100
        if direction == 'L':
            step1 = dial - dist
            if step1 <= 0:
                result += int(-step1 / 100) + (0 if dial == 0 else 1)
            dial = step1 % 100
    print(result)
    return result


if __name__ == '__main__':
    assert part1('test_input') == 3
    assert part1('input') == 1029
    assert part2('test_input') == 6
    assert part2('input') == 5892
