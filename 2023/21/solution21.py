def solve(filename):
    with (open(filename) as file):
        lines = file.read().splitlines()
        matrix = [list(line) for line in lines]

        sr, sc = next((i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == 'S')

        matrix[sr][sc] = '.'  # start is garden plot

        positions = {(sr, sc)}
        for _ in range(64):
            new_positions = set()
            for (r, c) in positions:
                for (rn, cn) in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= rn < len(matrix) and 0 <= cn < len(matrix[0]) and matrix[rn][cn] == '.':
                        new_positions.add((rn, cn))
            positions = new_positions
        print(len(positions))


if __name__ == '__main__':
    solve('test_input')
    solve('input')
