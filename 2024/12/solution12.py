DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def visit(matrix, visited, i, j):
    letter = matrix[i][j]
    visited[i][j] = True
    area = 1
    fences = []
    for di, dj in DIR:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]):
            if matrix[ni][nj] == letter and not visited[ni][nj]:
                (a, f) = visit(matrix, visited, ni, nj)
                area += a
                fences += f
            if matrix[ni][nj] != letter:
                fences.append(((i, j), (di, dj)))
        else:
            fences.append(((i, j), (di, dj)))
    return area, fences


def count_sides(fences: list[tuple[tuple[int, int], tuple[int, int]]]):
    cnt = 0
    for d in DIR:
        cnt += 1
        f = [pos for (pos, dir) in fences if dir == d]
        if d[0] != 0:
            f.sort()
            for i in range(1, len(f)):
                if f[i - 1][0] != f[i][0] or f[i - 1][1] != f[i][1] - 1:
                    cnt += 1
        else:
            f.sort(key=lambda x: (x[1], x[0]))
            for i in range(1, len(f)):
                if f[i - 1][1] != f[i][1] or f[i - 1][0] != f[i][0] - 1:
                    cnt += 1
    return cnt


def solve(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()
        matrix = [list(line) for line in lines]

        visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        price_1 = 0
        price_2 = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not visited[i][j]:
                    area, fences = visit(matrix, visited, i, j)
                    price_1 += area * len(fences)
                    price_2 += area * count_sides(fences)

        print(price_1)
        print(price_2)


if __name__ == '__main__':
    solve('test_input')  # 1930, 1206
    solve('input')  # 1477924, 841934
