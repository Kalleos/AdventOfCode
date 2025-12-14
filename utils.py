def print_matrix(matrix):
    if len(matrix) > 0:
        max_length = max([max([len(str(c)) for c in row]) for row in matrix])
        print('#' * ((max_length + 1) * len(matrix[0])))
        for row in matrix:
            print(' '.join([str(c).rjust(max_length, ' ') for c in row]))
        print('#' * ((max_length + 1) * len(matrix[0])))
    else:
        print('[]')


def get_dimensions(matrix):
    return len(matrix), len(matrix[0])


def find_all_in_matrix(matrix, c):
    return [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == c]
