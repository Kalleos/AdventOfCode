def solve(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()
        matrix = [list(line) for line in lines]

        n = len(matrix)
        m = len(matrix[0])

        # Part 1
        cnt = 0
        for i in range(n):
            for j in range(m):
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if 0 <= i + 3 * di < n and 0 <= j + 3 * dj < m and matrix[i][j] == 'X' and matrix[i + di][
                            j + dj] == 'M' and matrix[i + 2 * di][j + 2 * dj] == 'A' and matrix[i + 3 * di][
                            j + 3 * dj] == 'S':
                            cnt += 1

        print(cnt)

        # Part 2
        cnt = 0
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if matrix[i][j] == 'A' and (
                        matrix[i - 1][j - 1] == 'M' and matrix[i + 1][j + 1] == 'S' or matrix[i - 1][j - 1] == 'S' and
                        matrix[i + 1][j + 1] == 'M') and (
                        matrix[i - 1][j + 1] == 'M' and matrix[i + 1][j - 1] == 'S' or matrix[i - 1][j + 1] == 'S' and
                        matrix[i + 1][j - 1] == 'M'):
                    cnt += 1

        print(cnt)


if __name__ == '__main__':
    solve('test_input')  # 18, 9
    solve('input')  # 2427, 1900
