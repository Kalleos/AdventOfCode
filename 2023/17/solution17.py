import heapq


def visit(matrix):
    dists = {}
    to_visit = [(0, 0, 0, 0, 0)]
    while len(to_visit) > 0:
        dist, i, j, dir, same = heapq.heappop(to_visit)
        if (i, j, dir, same) in dists:
            continue

        dists[(i, j, dir, same)] = dist

        for new_dir, (dr, dc) in enumerate([(0, 1), (1, 0), (0, -1), (-1, 0)]):
            new_i = i + dr
            new_j = j + dc
            new_same = 1 if new_dir != dir else same + 1
            is_back = (dir - new_dir) % 4 == 2
            if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0]) and not is_back and new_same <= 3:
                heapq.heappush(to_visit, (dist + matrix[new_i][new_j], new_i, new_j, new_dir, new_same))

    result = min([dist for (i, j, _, _), dist in dists.items() if i == len(matrix) - 1 and j == len(matrix[0]) - 1])
    print(result)


def solve(filename):
    with (open(filename) as file):
        lines = file.read().splitlines()
        matrix = [[int(c) for c in line] for line in lines]
        visit(matrix)


if __name__ == '__main__':
    solve('test_input')
    solve('input')
