
def print_matrix(matrix):
    print('############################')
    for row in matrix:
        print(' '.join([str(c) for c in row]))
    print('############################')