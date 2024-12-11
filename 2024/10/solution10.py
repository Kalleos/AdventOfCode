DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def is_inside(pos, matrix):
    return 0 <= pos[0] < len(matrix) and 0 <= pos[1] < len(matrix[0])


def get_height(pos, matrix):
    return matrix[pos[0]][pos[1]]


def walk(matrix, pos, start):
    h = get_height(pos, matrix)
    if h == 9:
        return [(start, pos)]
    paths = []
    for d in DIR:
        new_pos = (pos[0] + d[0], pos[1] + d[1])
        if is_inside(new_pos, matrix) and get_height(new_pos, matrix) == h + 1:
            paths = paths + walk(matrix, new_pos, start)
    return paths


def solve(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()
        matrix = [list(map(int, list(line))) for line in lines]

        trailheads = set()
        for (i, row) in enumerate(matrix):
            for (j, cell) in enumerate(row):
                if cell == 0:
                    trailheads.add((i, j))

        paths = []
        for head in trailheads:
            paths.extend(walk(matrix, head, head))

        print(len(set(paths)))
        print(len(paths))


if __name__ == '__main__':
    solve('test_input')  # 36, 81
    solve('input')  # 674, 1372
