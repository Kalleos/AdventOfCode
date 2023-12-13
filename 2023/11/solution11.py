def expand_universe(universe: list[list[str]]):
    rows = []
    for i in range(len(universe)):
        if all([c == '.' for c in universe[i]]):
            rows.append(i)

    cols = []
    for i in range(len(universe[0])):
        if all([universe[j][i] == '.' for j in range(len(universe))]):
            cols.append(i)

    return rows, cols


def find_galaxies(universe: list[list[str]]):
    galaxies = []
    for i in range(len(universe)):
        for j in range(len(universe[0])):
            if universe[i][j] == '#':
                galaxies.append((i, j))
    return galaxies


def find_distances(galaxies: list[tuple[int]], empty_spaces, expansion: int):
    (empty_rows, empty_cols) = empty_spaces
    sum_dist = 0
    for i in range(len(galaxies)):
        for j in range(i):
            (x1, y1) = galaxies[i]
            (x2, y2) = galaxies[j]
            temp_empty_rows = [x for x in empty_rows if min(x1, x2) < x < max(x1, x2)]
            temp_empty_cols = [y for y in empty_cols if min(y1, y2) < y < max(y1, y2)]
            empties = len(temp_empty_cols) + len(temp_empty_rows)

            distance = abs(x1 - x2) + abs(y1 - y2) + empties * (expansion - 1)
            #print(i, j, empties, distance)
            sum_dist += distance
    return sum_dist


def solve(filename):
    with (open(filename) as file):
        lines = file.read().splitlines()
        universe = [[c for c in row] for row in lines]
        empties = expand_universe(universe)
        galaxies = find_galaxies(universe)

        # print_matrix(universe)
        # print_matrix(galaxies)

        print(find_distances(galaxies, empties, 2))
        print(find_distances(galaxies, empties, 10))
        print(find_distances(galaxies, empties, 100))
        print(find_distances(galaxies, empties, 1000000))


if __name__ == '__main__':
    solve('test_input') # 374
    solve('input') # 9965032
