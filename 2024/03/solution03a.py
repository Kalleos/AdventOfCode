import re


def solve(filename: str):
    with open(filename) as file:
        data = file.read()
        result = 0
        for m in re.finditer("mul\((\d{1,3}),(\d{1,3})\)", data):
            result += int(m.group(1)) * int(m.group(2))
    print(result)


if __name__ == '__main__':
    solve('test_input')
    solve('input')
