dirs = {(-1, 0): '^', (0, 1): '>', (1, 0): 'v', (0, -1): '<'}


def solve(filename):
    with (open(filename) as file):
        lines = file.read().splitlines()
        matrix = [list(line) for line in lines]

        max_length = 0
        start = (0, 1)
        to_visit = [(start, [start])]
        while to_visit:
            (r, c), visited = to_visit.pop()
            if r == len(matrix) - 1 and c == len(matrix[0]) - 2:
                length = len(visited) - 1
                max_length = max(max_length, length)
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]) and matrix[nr][nc] in ['.', dirs[(dr, dc)]] and (
                        nr, nc) not in visited:
                    to_visit.append(((nr, nc), visited + [(nr, nc)]))

        print(max_length)


if __name__ == '__main__':
    solve('test_input')
    solve('input')
