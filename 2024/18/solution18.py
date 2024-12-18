DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def parse_input(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()
        return [map(int, line.split(",")) for line in lines]


def find_shortest_path(memory: list[list[str]], start: tuple[int, int], end: tuple[int, int]):
    distances = {start: 0}
    queue = [start]
    while queue:
        (x, y) = queue.pop(0)
        if (x, y) == end:
            return distances[(x, y)]
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(memory) and 0 <= ny < len(memory):
                if memory[ny][nx] == '.' and ((nx, ny) not in distances or distances[(x, y)] + 1 < distances[(nx, ny)]):
                    distances[(nx, ny)] = distances[(x, y)] + 1
                    queue.append((nx, ny))


def solve(filename: str, n: int, k: int):
    coordinates = parse_input(filename)

    memory = [['.' for _ in range(n)] for _ in range(n)]
    for x, y in coordinates[:k]:
        memory[y][x] = '#'
    distance = find_shortest_path(memory, (0, 0), (n - 1, n - 1))
    print(distance)

    for x, y in coordinates[k:]:
        memory[y][x] = '#'
        distance = find_shortest_path(memory, (0, 0), (n - 1, n - 1))
        if distance is None:
            print(f"{x},{y}")
            break


if __name__ == '__main__':
    solve('test_input', 7, 12)
    solve('input', 71, 1024)
