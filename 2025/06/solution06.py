import math


def parse_input(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()
        max_length = max([len(line) for line in lines])
        return [line.rjust(max_length) for line in lines]


def part1(filename: str):
    worksheet = parse_input(filename)
    ns_rows = [[int(n) for n in row.split()] for row in worksheet[:-1]]
    ops = worksheet[-1].split()
    result = 0
    for i, op in enumerate(ops):
        nums = [row[i] for row in ns_rows]
        if op == '*':
            result += math.prod(nums)
        if op == '+':
            result += sum(nums)
    print(result)
    return result


def part2(filename: str):
    worksheet = parse_input(filename)
    ns_rows = worksheet[:-1]
    ops = worksheet[-1]
    result = 0
    temp = 0
    act_op = None
    for i, op in enumerate(ops):
        num_s = "".join([row[i] for row in ns_rows]).strip()
        if not num_s:
            continue
        num = int(num_s)
        if op in ['+', '*']:
            result += temp
            act_op = op
            temp = num
        else:
            if act_op == '*':
                temp *= num
            if act_op == '+':
                temp += num
    result += temp
    print(result)
    return result


if __name__ == '__main__':
    assert part1('test_input') == 4277556
    part1('input')
    assert part2('test_input') == 3263827
    part2('input')
