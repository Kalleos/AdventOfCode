from utils import print_matrix


def read_matrices(lines):
    matrices = []
    matrix = []
    for line in lines:
        if line.strip() == "":
            matrices.append(matrix)
            matrix = []
        else:
            matrix.append(line)

    matrices.append(matrix)
    return matrices


def get_column(m, c):
    return [r[c] for r in m]


def difference(l1, l2):
    return sum([0 if x == y else 1 for x, y in zip(l1, l2)])


def get_vertical_mirror(m, diff):
    for i in range(1, len(m[0])):
        if sum([difference(get_column(m, i - k - 1), get_column(m, i + k)) for k in range(min(i, len(m[0]) - i))]) == diff:
            return i


def get_horizontal_mirror(m, diff):
    for i in range(1, len(m)):
        if sum([difference(m[i - k - 1], m[i + k]) for k in range(min(i, len(m) - i))]) == diff:
            return i


def solve(filename, diff):
    with (open(filename) as file):
        lines = file.read().splitlines()
        ms = read_matrices(lines)

        result = 0
        for m in ms:
            v = get_vertical_mirror(m, diff)
            if v:
                result += v
            else:
                h = get_horizontal_mirror(m, diff)
                if h:
                    result += 100 * h
                else:
                    print_matrix(m)
                    raise ValueError('something went wrong')
        print(result)


if __name__ == '__main__':
    solve('test_input', 0) # 405
    solve('input', 0) # 32035
    solve('test_input', 1)
    solve('input', 1)
