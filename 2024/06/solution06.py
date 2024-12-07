def find_start(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '<':
                return i, j, (0, -1)
            if matrix[i][j] == '>':
                return i, j, (0, 1)
            if matrix[i][j] == '^':
                return i, j, (-1, 0)
            if matrix[i][j] == 'v':
                return i, j, (1, 0)


def rotate(d):
    if d == (0, -1):
        return -1, 0
    if d == (-1, 0):
        return 0, 1
    if d == (0, 1):
        return 1, 0
    if d == (1, 0):
        return 0, -1


def find_out(matrix):
    (i, j, d) = find_start(matrix)
    visited = set()
    visited_dir = set()
    while True:
        visited.add((i, j))
        visited_dir.add((i, j, d))
        (ni, nj) = (i + d[0], j + d[1])
        if not (0 <= ni < len(matrix) and 0 <= nj < len(matrix[0])):
            break

        while matrix[ni][nj] == '#':
            d = rotate(d)
            (ni, nj) = (i + d[0], j + d[1])
        (i, j) = (ni, nj)
        if (i, j, d) in visited_dir:
            return None
    return visited


def solve(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()
        matrix = [list(line) for line in lines]

        # Part 1
        visited = find_out(matrix)
        print(len(visited))

        # Part 2
        cnt = 0
        for (i, j) in visited:
            if matrix[i][j] == '.':
                matrix[i][j] = '#'
                if find_out(matrix) is None:
                    cnt += 1
                matrix[i][j] = '.'
        print(cnt)


if __name__ == '__main__':
    solve('test_input')  # 41, 6
    solve('input')  # 4647, 1723
