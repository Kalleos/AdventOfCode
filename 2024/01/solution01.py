def solve(filename: str):
    left = []
    right = []
    with open(filename) as file:
        lines = file.read().splitlines()
        for line in lines:
            left_num, right_num = map(int, line.split())
            left.append(left_num)
            right.append(right_num)

    part1(left, right)
    part2(left, right)


def part1(left: list[int], right: list[int]):
    left_sorted = sorted(left)
    right_sorted = sorted(right)
    diff = sum([abs(r - l) for (l, r) in zip(left_sorted, right_sorted)])
    print(diff)


def part2(left: list[int], right: list[int]):
    sim = sum([l * right.count(l) for l in left])
    print(sim)

if __name__ == '__main__':
    solve('test_input') # 11, 31
    solve('input') # 1765812, 20520794
