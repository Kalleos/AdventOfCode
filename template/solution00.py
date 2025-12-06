def parse_input(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()


def solve(filename: str):
    data = parse_input(filename)
    result = 0

    print(result)
    return result


if __name__ == '__main__':
    assert solve('test_input') == 0
    # solve('input')
