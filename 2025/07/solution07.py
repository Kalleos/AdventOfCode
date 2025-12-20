from utils import find_all_in_matrix


def parse_input(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()
        matrix = [list(line) for line in lines]
        return matrix


def part1(filename: str):
    matrix = parse_input(filename)
    (xs, ys) = find_all_in_matrix(matrix, 'S')[0]
    result = 0
    beam = {ys}
    for x in range(xs + 1, len(matrix)):
        new_beam = set()
        for y in beam:
            if matrix[x][y] == '.':
                new_beam.add(y)
            if matrix[x][y] == '^':
                result += 1
                new_beam.add(y - 1)
                new_beam.add(y + 1)
        beam = new_beam
    print(result)
    return result


def part2(filename: str):
    matrix = parse_input(filename)
    (xs, ys) = find_all_in_matrix(matrix, 'S')[0]
    n = len(matrix[0])
    beam = [0] * n
    beam[ys] = 1
    for x in range(xs + 1, len(matrix)):
        new_beam = [0] * n
        for y in range(n):
            if matrix[x][y] == '.':
                new_beam[y] += beam[y]
            if matrix[x][y] == '^':
                new_beam[y - 1] += beam[y]
                new_beam[y + 1] += beam[y]
        beam = new_beam
    result = sum(beam)
    print(result)
    return result


if __name__ == '__main__':
    assert part1('test_input') == 21
    assert part1('input') == 1649
    assert part2('test_input') == 40
    assert part2('input') == 16937871060075
