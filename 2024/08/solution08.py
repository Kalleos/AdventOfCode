def solve(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()

        n = len(lines)
        m = len(lines[0])
        antennas = {}
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char != '.':
                    if antennas.get(char) is None:
                        antennas[char] = [(i, j)]
                    else:
                        antennas[char].append((i, j))

        # Part 1
        antinodes = set()
        for char in antennas:
            for k in range(len(antennas[char])):
                for l in range(len(antennas[char])):
                    if k != l:
                        (i1, j1) = antennas[char][k]
                        (i2, j2) = antennas[char][l]

                        (di, dj) = (i2 - i1, j2 - j1)

                        (a, b) = (i1 - di, j1 - dj)
                        if 0 <= a < n and 0 <= b < m:
                            antinodes.add((a, b))
        print(len(antinodes))

        # Part 2
        antinodes = set()
        for char in antennas:
            for k in range(len(antennas[char])):
                for l in range(len(antennas[char])):
                    if k != l:
                        (i1, j1) = antennas[char][k]
                        (i2, j2) = antennas[char][l]

                        (di, dj) = (i2 - i1, j2 - j1)

                        for i in range(abs(int(min(n / di, m / dj)))):
                            (a, b) = (i1 - i * di, j1 - i * dj)
                            if 0 <= a < n and 0 <= b < m:
                                antinodes.add((a, b))
                            else:
                                break
        print(len(antinodes))


if __name__ == '__main__':
    solve('test_input')  # 14, 34
    solve('input')  # 280, 958
