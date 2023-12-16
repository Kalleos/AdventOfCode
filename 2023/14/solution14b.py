def tilt(matrix, dir):
    result = matrix
    reverse = False
    if dir in ['N', 'S']:
        result = zip(*result)
    if dir in ['N', 'W']:
        reverse = True
    result = ["#".join(["".join(sorted(a, reverse=reverse)) for a in "".join(col).split('#')]) for col in result]

    if dir in ['N', 'S']:
        new_result = []
        for row in zip(*result):
            new_result.append(row)
        result = new_result
    return result


def get_loads(matrix):
    return sum([row.count('O') * (len(matrix) - k) for (k, row) in enumerate(matrix)])


def solve(filename):
    with (open(filename) as file):
        lines = file.read().splitlines()

        matrix = lines
        loads = [0]
        cache = {}
        for n in range(1000000000):
            if tuple(matrix) in cache:
                period_start = cache.get(tuple(matrix))
                period_length = n - period_start
                print(loads[(1000000000 - (period_start - 1)) % period_length + (period_start - 1)])
                break
            cache[tuple(matrix)] = n
            matrix = tilt(matrix, 'N')
            matrix = tilt(matrix, 'W')
            matrix = tilt(matrix, 'S')
            matrix = tilt(matrix, 'E')
            load = get_loads(list(matrix))
            loads.append(load)


if __name__ == '__main__':
    solve('test_input')
    solve('input')
