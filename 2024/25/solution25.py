def parse_input(filename: str):
    with open(filename) as file:
        blocks = file.read().split("\n\n")

        locks = []
        keys = []

        for block in blocks:
            rows = block.splitlines()

            columns = [0] * 5
            for row in rows[1:-1]:
                columns = [a + b for a, b in zip(columns, [1 if c == '#' else 0 for c in row])]

            if rows[0] == "#####":
                locks.append(columns)
            else:
                keys.append(columns)

        return locks, keys


def fits(lock, key):
    for c in range(5):
        if lock[c] + key[c] > 5:
            return False
    return True


def solve(filename: str):
    locks, keys = parse_input(filename)
    result = sum([fits(lock, key) for lock in locks for key in keys])
    print(result)


if __name__ == '__main__':
    solve('test_input')
    solve('input')
