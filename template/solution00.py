def parse_input(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()


def solve(filename: str):
    parse_input(filename)


if __name__ == '__main__':
    solve('test_input')
    # solve('input')
