def visit(matrix: list[list[str]], visited: list[list[list[str]]], i: int, j: int, dir: str):
    to_visit = [(i, j, dir)]
    while len(to_visit) > 0:
        (i, j, dir) = to_visit.pop()

        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or dir in visited[i][j]:
            continue
        visited[i][j].append(dir)

        f = matrix[i][j]
        if f == '.':
            new_i = i
            new_j = j
            if dir == 'R':
                new_j += 1
            if dir == 'L':
                new_j -= 1
            if dir == 'D':
                new_i += 1
            if dir == 'U':
                new_i -= 1
            to_visit.append((new_i, new_j, dir))

        if f == '/':
            new_i = i
            new_j = j
            new_dir = ''
            if dir == 'R':
                new_i -= 1
                new_dir = 'U'
            if dir == 'L':
                new_i += 1
                new_dir = 'D'
            if dir == 'D':
                new_j -= 1
                new_dir = 'L'
            if dir == 'U':
                new_j += 1
                new_dir = 'R'
            to_visit.append((new_i, new_j, new_dir))

        if f == '\\':
            new_i = i
            new_j = j
            new_dir = ''
            if dir == 'R':
                new_i += 1
                new_dir = 'D'
            if dir == 'L':
                new_i -= 1
                new_dir = 'U'
            if dir == 'D':
                new_j += 1
                new_dir = 'R'
            if dir == 'U':
                new_j -= 1
                new_dir = 'L'
            to_visit.append((new_i, new_j, new_dir))

        if f == '|':
            new_i = i
            new_j = j
            if dir in ['R', 'L']:
                to_visit.append((i - 1, j, 'U'))
                to_visit.append((i + 1, j, 'D'))
            if dir == 'D':
                new_i += 1
            if dir == 'U':
                new_i -= 1
            to_visit.append((new_i, new_j, dir))

        if f == '-':
            new_i = i
            new_j = j
            if dir == 'R':
                new_j += 1
                to_visit.append((new_i, new_j, dir))
            if dir == 'L':
                new_j -= 1
                to_visit.append((new_i, new_j, dir))
            if dir in ['D', 'U']:
                to_visit.append((i, j - 1, 'L'))
                to_visit.append((i, j + 1, 'R'))


def get_max_energized(matrix, configs):
    max_energized = 0

    for config in configs:
        (i, j, dir) = config
        visited = [[[] for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        visit(matrix, visited, i, j, dir)
        tiles_energized = sum(
            [sum([1 for j in range(len(visited[0])) if len(visited[i][j]) > 0]) for i in range(len(visited))])
        max_energized = tiles_energized if tiles_energized > max_energized else max_energized

    return max_energized


def solve(filename):
    with (open(filename) as file):
        lines = file.read().splitlines()
        matrix = [list(line) for line in lines]
        # Part 1
        configs = [(0, 0, 'R')]
        print(get_max_energized(matrix, configs))
        # Part 2
        configs = [(0, j, 'D') for j in range(len(matrix[0]))] + [(len(matrix) - 1, j, 'U') for j in range(len(matrix[0]))] + [(i, 0, 'R') for i in range(len(matrix))] + [(i, len(matrix[0]) - 1, 'L') for i in range(len(matrix))]
        print(get_max_energized(matrix, configs))


if __name__ == '__main__':
    solve('test_input')
    solve('input')
