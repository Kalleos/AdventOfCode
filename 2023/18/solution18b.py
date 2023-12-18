dirs = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}


def solve(filename):
    with (open(filename) as file):
        lines = file.read().splitlines()
        plan = [line.split(' ')[2] for line in lines]
        plan = [(list(dirs)[int(h[7])], int(h[2:7], 16)) for h in plan]

        points = [(0, 0)]
        u = 0
        for step in plan:
            (i, j) = points[-1]
            (dr, dc) = dirs.get(step[0])
            n = step[1]
            u += n
            points.append((i + n * dr, j + n * dc))

        N = len(points)

        A = sum([(points[i][1] * points[(i + 1) % N][0] - points[i][0] * points[(i + 1) % N][1]) for i in range(N)]) // 2
        #print(A)
        #print(u)
        print(A + u // 2 + 1)


if __name__ == '__main__':
    solve('test_input')
    solve('input')
