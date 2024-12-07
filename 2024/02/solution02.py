def is_safe_part1(report: list[int]):
    diffs = [(a - b) for (a, b) in zip(report[:-1], report[1:])]
    return all([l in [1, 2, 3] for l in diffs]) or all([l in [-1, -2, -3] for l in diffs])


def is_safe_part2(report: list[int]):
    for i in range(len(report)):
        if is_safe_part1(report[:i] + report[i + 1:]):
            return True
    return False


def solve(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()
        reports = [list(map(int, line.split())) for line in lines]
        print(sum(is_safe_part1(report) for report in reports))
        print(sum(is_safe_part2(report) for report in reports))


if __name__ == '__main__':
    solve('test_input')  # 2, 4
    solve('input')  # 369, 428
