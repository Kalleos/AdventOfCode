def solve(filename):
    with (open(filename) as file):
        lines = file.read().splitlines()
        n = len(lines)
        result = 0
        for col in zip(*lines):
            tilted = "#".join(["".join(sorted(a, reverse=True)) for a in "".join(col).split('#')])
            loads = [(n - i) for (i, c) in enumerate(tilted) if c == 'O']
            result += sum(loads)
        print(result)


if __name__ == '__main__':
    solve('test_input')
    solve('input')
