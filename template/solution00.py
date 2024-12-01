def solve(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()


if __name__ == '__main__':
    solve('test_input')
    # solve('input')
