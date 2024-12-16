DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
FORWARD_COST = 1
TURN_COST = 1001


def parse_input(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()
        matrix = [list(line) for line in lines]
        return matrix


def turn(direction, lr):
    return DIRECTIONS[(DIRECTIONS.index(direction) + lr) % 4]


def visit(matrix, costs, x, y, direction):
    if matrix[x][y] == 'E':
        return []

    to_visit = []

    for (new_direction, extra_cost) in [
        (direction, FORWARD_COST),  # forward
        (turn(direction, -1), TURN_COST),  # turn left
        (turn(direction, 1), TURN_COST)  # turn right
    ]:
        nx, ny = x + new_direction[0], y + new_direction[1]
        cost = costs[x][y] + extra_cost
        if matrix[nx][ny] != '#' and (costs[nx][ny] == 0 or cost < costs[nx][ny]):
            costs[nx][ny] = cost
            to_visit.append((nx, ny, new_direction))

    return to_visit


def mark_seats(matrix, costs, x, y, direction, cost):
    for (new_direction, extra_cost) in [
        (direction, FORWARD_COST),  # forward
        (turn(direction, -1), TURN_COST),  # turn left
        (turn(direction, 1), TURN_COST)  # turn right
    ]:
        nx, ny = x + new_direction[0], y + new_direction[1]
        if matrix[nx][ny] == '.' and costs[nx][ny] <= cost - extra_cost:
            matrix[nx][ny] = 'O'
            mark_seats(matrix, costs, nx, ny, new_direction, cost - extra_cost)


def find_all_in_matrix(matrix, c):
    return [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == c]


def solve(filename: str):
    matrix = parse_input(filename)
    costs = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    (xs, ys) = find_all_in_matrix(matrix, 'S')[0]

    to_visit = {(xs, ys, DIRECTIONS[0])}
    while len(to_visit) > 0:
        (xs, ys, direction) = to_visit.pop()
        to_visit.update(visit(matrix, costs, xs, ys, direction))

    (xe, ye) = find_all_in_matrix(matrix, 'E')[0]
    print(costs[xe][ye])

    for direction in DIRECTIONS:
        mark_seats(matrix, costs, xe, ye, direction, costs[xe][ye])

    print(len(find_all_in_matrix(matrix, 'O')) + 2)


if __name__ == '__main__':
    solve('test_input')
    solve('test_input2')
    solve('input')
