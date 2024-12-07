import re


def solve(filename: str):
    with open(filename) as file:
        data = file.read()
        result = 0
        do = True
        for m in re.finditer("mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)", data):
            if m.group(0) == "do()":
                do = True
                continue
            if m.group(0) == "don't()":
                do = False
                continue
            if do:
                result += int(m.group(1)) * int(m.group(2))
    print(result)


if __name__ == '__main__':
    solve('test_input2')
    solve('input')
