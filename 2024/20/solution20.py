from collections import Counter

from utils import get_dimensions

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def parse_input(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()
        matrix = [list(line) for line in lines]
        return matrix


def visit(matrix, x, y):
    costs = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    to_visit = [(x, y)]

    while len(to_visit) > 0:
        (x, y) = to_visit.pop()

        if matrix[x][y] == 'E':
            return costs

        for direction in DIRECTIONS:
            nx, ny = x + direction[0], y + direction[1]
            if matrix[nx][ny] in ['.', 'E'] and (costs[nx][ny] == 0 or costs[x][y] + 1 < costs[nx][ny]):
                costs[nx][ny] = costs[x][y] + 1
                to_visit.append((nx, ny))


def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def solve(filename: str, min_save: int, cheat_length: int):
    matrix = parse_input(filename)
    (n, m) = get_dimensions(matrix)
    (xs, ys) = [(i, j) for i in range(n) for j in range(m) if matrix[i][j] == 'S'][0]

    costs = visit(matrix, xs, ys)
    cnt = 0
    cheats = []
    for x1 in range(1, n - 1):
        for y1 in range(1, m - 1):
            if matrix[x1][y1] != '#':

                for x2 in range(x1, n - 1):
                    y2_start = y1 if x1 == x2 else 1
                    for y2 in range(y2_start, m - 1):
                        if matrix[x2][y2] != '#':
                            dist = distance(x1, y1, x2, y2)
                            if 2 <= dist <= cheat_length:

                                cheat = abs(costs[x1][y1] - costs[x2][y2]) - dist
                                if cheat >= min_save:
                                    cheats.append(cheat)
                                    cnt += 1

    print(cnt)
    print(Counter(cheats))


if __name__ == '__main__':
    solve('test_input', 2, 2)
    solve('input', 100, 2)

    solve('test_input', 50, 20)
    solve('input', 100, 20)
