def parse_input(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()
        lines = [list(row.strip()) for row in lines]
        return lines


def cnt_rolls(grid):
    return sum([sum([c == '@' for c in row]) for row in grid])


def cnt_rolls_in_sub(grid, i, j):
    h = len(grid)
    w = len(grid[0])
    sub = [
        grid[r][max(j - 1, 0):min(j + 2, w)]
        for r in range(max(i - 1, 0), min(i + 2, h))
    ]
    return cnt_rolls(sub)


def solve(filename: str, remove: bool):
    result = 0
    grid = parse_input(filename)
    while True:
        removed = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == '@' and cnt_rolls_in_sub(grid, i, j) <= 4:
                    result += 1
                    if remove:
                        grid[i][j] = 'x'
                        removed += 1
        if not remove or removed == 0:
            break
    print(result)
    return result


if __name__ == '__main__':
    assert solve('test_input', False) == 13
    solve('input', False)
    assert solve('test_input', True) == 43
    solve('input', True)
