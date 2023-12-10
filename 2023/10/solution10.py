directions = {
    'S': [(1, 0), (0, -1), (-1, 0), (0, 1)],
    '|': [(0, 1), (0, -1)],
    '-': [(1, 0), (-1, 0)],
    'F': [(1, 0), (0, 1)],
    '7': [(-1, 0), (0, 1)],
    'L': [(0, -1), (1, 0)],
    'J': [(-1, 0), (0, -1)],
    '.': []
}


def find_distances(matrix, distances, x, y):
    to_visit = [(x, y)]
    while len(to_visit) > 0:
        (x, y) = to_visit.pop(0)
        for dir in directions[matrix[y][x]]:
            new_x = x + dir[0]
            new_y = y + dir[1]
            if 0 <= new_x < len(matrix[0]) and 0 <= new_y < len(matrix) and distances[new_y][new_x] == 0 and \
                    matrix[new_y][new_x] not in ['S', '.']:
                if (-1 * dir[0], -1 * dir[1]) in directions[matrix[new_y][new_x]]:
                    distances[new_y][new_x] = distances[y][x] + 1
                    to_visit.append((new_x, new_y))
    return max([max(row) for row in distances])


def find_s(matrix):
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if char == 'S':
                return (j, i)
    return None  # character is not found


def create_filled_matrix(m, n, fill_with):
    return [[fill_with] * n for _ in range(m)]


def switch_i_o(i_o):
    return 'I' if i_o == 'O' else 'O'


def get_inside_outside(matrix, distances):
    i_o_matrix = create_filled_matrix(len(distances[0]), len(distances), ' ')
    for i in range(len(distances)):
        i_o = 'O'
        edge_start = None
        for j in range(len(distances[0])):
            if distances[i][j] == 0:
                i_o_matrix[i][j] = i_o
            else:
                if matrix[i][j] in ['F', 'L']:
                    edge_start = matrix[i][j]
                if matrix[i][j] == '7' and edge_start == 'L' or matrix[i][j] == 'J' and edge_start == 'F' or matrix[i][j] == '|':
                    """
                                            |                                               |                         |
                      -->                   L----7                                    F----J                          |
                                                 |                                    |                               |
                    """
                    i_o = switch_i_o(i_o)

    return i_o_matrix


def print_matrix(matrix):
    print('############################')
    for row in matrix:
        print(' '.join([str(c) for c in row]))
    print('############################')


def replace_s(matrix, distances, start):
    (x, y) = start
    distances[y][x] = -1

    if 0 < y < len(matrix) - 1 and distances[y - 1][x] == 1 and distances[y + 1][x] == 1:
        matrix[y][x] = '|'
    if 0 < x < len(matrix[0]) - 1 and distances[y][x - 1] == 1 and distances[y][x - 1] == 1:
        matrix[y][x] = '-'
    if y > 0 and x < len(matrix[0]) - 1 and distances[y - 1][x] == 1 and distances[y][x + 1] == 1:
        matrix[y][x] = 'L'
    if y < len(matrix) - 1 and x < len(matrix[0]) - 1 and distances[y + 1][x] == 1 and distances[y][x + 1] == 1:
        matrix[y][x] = 'F'
    if y > 0 and x > 0 and distances[y - 1][x] == 1 and distances[y][x - 1] == 1:
        matrix[y][x] = 'J'
    if y < len(matrix) - 1 and x > 0 and distances[y][x - 1] == 1 and distances[y + 1][x] == 1:
        matrix[y][x] = '7'
    if matrix[y][x] == 'S':
        raise ValueError('Something went wrong')


def solve(filename):
    with (open(filename) as file):
        matrix = []
        for line in file.read().splitlines():
            matrix.append(list(line))

        #print_matrix(matrix)
        (start_x, start_y) = find_s(matrix)
        print((start_x, start_y))

        distances = create_filled_matrix(len(matrix[0]), len(matrix), 0)
        max_distance = find_distances(matrix, distances, start_x, start_y)
        print_matrix(distances)
        print(max_distance)
        replace_s(matrix, distances, (start_x, start_y))
        #print_matrix(matrix)
        i_o_matrix = get_inside_outside(matrix, distances)
        print_matrix(i_o_matrix)
        print(sum([1 for i in range(len(i_o_matrix)) for j in range(len(i_o_matrix[0])) if i_o_matrix[i][j] == 'I']))


if __name__ == '__main__':
    solve('test_input')
    solve('input')
