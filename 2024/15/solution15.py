DIRECTIONS = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}

EMPTY = '.'
ROBOT = '@'
WALL = '#'
BOX = 'O'
BOX_LEFT = '['
BOX_RIGHT = ']'


def can_move(position: tuple[int, int], direction: str, warehouse: list[list[str]]):
    next_position = (position[0] + DIRECTIONS[direction][0], position[1] + DIRECTIONS[direction][1])
    next_tile = warehouse[next_position[0]][next_position[1]]
    if next_tile == EMPTY:
        return True
    if next_tile == WALL:
        return False
    if next_tile == BOX or direction in ['<', '>']:
        return can_move(next_position, direction, warehouse)
    if next_tile == BOX_LEFT:
        return can_move(next_position, direction, warehouse) and can_move((next_position[0], next_position[1] + 1),
                                                                          direction, warehouse)
    if next_tile == BOX_RIGHT:
        return can_move(next_position, direction, warehouse) and can_move((next_position[0], next_position[1] - 1),
                                                                          direction, warehouse)


def move(position: tuple[int, int], direction: str, warehouse: list[list[str]]):
    next_position = (position[0] + DIRECTIONS[direction][0], position[1] + DIRECTIONS[direction][1])
    next_tile = warehouse[next_position[0]][next_position[1]]
    if next_tile == BOX:
        move(next_position, direction, warehouse)
    if next_tile == BOX_LEFT:
        move((next_position[0], next_position[1] + 1), direction, warehouse)
        move(next_position, direction, warehouse)
    if next_tile == BOX_RIGHT:
        move((next_position[0], next_position[1] - 1), direction, warehouse)
        move(next_position, direction, warehouse)
    warehouse[next_position[0]][next_position[1]] = warehouse[position[0]][position[1]]
    warehouse[position[0]][position[1]] = EMPTY
    return next_position


def spread(line: str):
    return line.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")


def parse_input_part1(filename: str):
    with open(filename) as file:
        blocks = file.read().split('\n\n')
        warehouse = [list(line) for line in blocks[0].splitlines()]
        movements = blocks[1].replace('\n', '')
        return warehouse, movements


def parse_input_part2(filename: str):
    with open(filename) as file:
        blocks = file.read().split('\n\n')
        warehouse = [list(spread(line)) for line in blocks[0].splitlines()]
        movements = blocks[1].replace('\n', '')
        return warehouse, movements


def solve(data):
    warehouse, movements = data
    w, h = len(warehouse[0]), len(warehouse)

    robot = [(i, j) for i in range(h) for j in range(w) if warehouse[i][j] == '@'][0]
    for d in movements:
        if can_move(robot, d, warehouse):
            robot = move(robot, d, warehouse)

    result = sum([100 * i + j for i in range(h) for j in range(w) if warehouse[i][j] in [BOX, BOX_LEFT]])
    print(result)


if __name__ == '__main__':
    solve(parse_input_part1('test_input'))
    solve(parse_input_part2('test_input'))

    solve(parse_input_part1('input'))
    solve(parse_input_part2('input'))
