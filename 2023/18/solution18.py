dirs = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}


def size(matrix):
    return sum([sum([1 for c in row if c == '#']) for row in matrix])


def find_inside(matrix):
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == '#' and row[j + 1] == '#':
                break
            if c == '#' and row[j + 1] == '.':
                return i, j + 1


def fill(matrix, i, j):
    to_visit = [(i, j)]
    while len(to_visit) > 0:
        (i, j) = to_visit.pop()
        matrix[i][j] = '#'

        for nb in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
            if matrix[nb[0]][nb[1]] == '.':
                to_visit.append(nb)


def solve(filename):
    with (open(filename) as file):
        lines = file.read().splitlines()
        plan = [tuple(line.split(' ')[0:2]) for line in lines]
        plan = [(d, int(s)) for (d, s) in plan]
        cols_left = sum(s for (d, s) in plan if d == 'L') + 1
        cols_right = sum(s for (d, s) in plan if d == 'R') + 1
        rows_up = sum(s for (d, s) in plan if d == 'U') + 1
        rows_downs = sum(s for (d, s) in plan if d == 'D') + 1
        cols = cols_left + cols_right
        rows = rows_up + rows_downs

        matrix = [['.' for _ in range(cols)] for _ in range(rows)]
        i = rows_up
        j = cols_left
        matrix[i][j] = '#'
        for step in plan:
            for _ in range(step[1]):
                (dr, dc) = dirs.get(step[0])
                i += dr
                j += dc
                matrix[i][j] = '#'
        print(size(matrix))
        inside = find_inside(matrix)
        fill(matrix, inside[0], inside[1])
        print(size(matrix))


if __name__ == '__main__':
    solve('test_input')
    solve('input')
