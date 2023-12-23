def solve(filename):
    with (open(filename) as file):
        lines = file.read().splitlines()
        matrix = [list(line) for line in lines]
        N = len(matrix)
        M = len(matrix[0])

        sr, sc = next((i, j) for i in range(N) for j in range(M) if matrix[i][j] == 'S')

        matrix[sr][sc] = '.'  # start is garden plot

        positions0 = set()
        positions1 = {(sr, sc)}
        pos_to_visit = {(sr, sc)}
        for _ in range(500):
            next_pos_to_visit = set()
            for (r, c) in pos_to_visit:
                for (rn, cn) in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if matrix[rn % N][cn % M] == '.':
                        if (rn,cn) not in positions0:
                            next_pos_to_visit.add((rn, cn))
                            positions0.add((rn, cn))
            pos_to_visit = next_pos_to_visit
            temp = positions0
            positions0 = positions1
            positions1 = temp
        print(len(positions1))


if __name__ == '__main__':
    solve('test_input')
    #solve('input')
