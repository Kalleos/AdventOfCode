dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def is_node(matrix: list[list[str]], r: int, c: int):
    N = len(matrix)
    M = len(matrix[0])
    return (r, c) == (0, 1) or (r, c) == (N - 1, M - 2) or len(
        [(r + dr, c + dc) for dr, dc in dirs if
         0 <= r + dr < N and 0 <= c + dc < M and matrix[r + dr][c + dc] != '#']) > 2


def create_graph(matrix: list[list[str]], start: tuple[int, int]) -> (list[tuple[int, int]], list[list[int]]):
    N = len(matrix)
    M = len(matrix[0])
    visited = []
    to_visit = [(start, start, 0)]
    dist_list = []
    nodes = {start}
    while to_visit:
        edge_start, (r, c), dist = to_visit.pop()
        visited.append((r, c))
        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M and matrix[nr][nc] != '#' and edge_start != (nr, nc):
                if is_node(matrix, nr, nc):
                    nodes.add((nr, nc))
                    dist_list.append((edge_start, (nr, nc), dist + 1))
                    if (nr, nc) not in visited:
                        to_visit.append(((nr, nc), (nr, nc), 0))
                elif (nr, nc) not in visited:
                    to_visit.append((edge_start, (nr, nc), dist + 1))

    distances = [[-1 for _ in range(len(nodes))] for _ in range(len(nodes))]
    for fn, tn, dist in dist_list:
        from_idx = list(nodes).index(fn)
        to_idx = list(nodes).index(tn)
        distances[from_idx][to_idx] = dist
        distances[to_idx][from_idx] = dist

    return nodes, distances


def solve(filename):
    with (open(filename) as file):
        lines = file.read().splitlines()
        matrix = [list(line) for line in lines]

        N = len(matrix)
        M = len(matrix[0])
        start = (0, 1)
        end = (N - 1, M - 2)

        (nodes, distances) = create_graph(matrix, start)

        start_idx = list(nodes).index(start)
        end_idx = list(nodes).index(end)

        max_length = 0
        to_visit = [(start_idx, [start_idx], 0)]
        while to_visit:
            node, visited, length = to_visit.pop()
            if node == end_idx and length > max_length:
                print(f'Found a way with a length of {length}')
                max_length = length
            for i in range(len(nodes)):
                if distances[node][i] > 0 and i not in visited:
                    to_visit.append((i, visited + [i], length + distances[node][i]))
        print(max_length)


if __name__ == '__main__':
    solve('test_input')
    solve('input')
