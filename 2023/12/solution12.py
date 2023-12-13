def get_counts(springs: str):
    return [len(s) for s in springs.split('.') if '#' in s]


def fits(springs: str, numbers: list[int]):
    return get_counts(springs) == numbers


def could_fit(springs: str, numbers: list[int]):
    return True


def get_arrangements(springs: str, numbers: list[int]):
    if '?' not in springs:
        return 1 if fits(springs, numbers) else 0

    arr = 0

    with_spring = springs.replace('?', '#', 1)
    if could_fit(with_spring, numbers):
        arr += get_arrangements(with_spring, numbers)

    with_no_spring = springs.replace('?', '.', 1)
    if could_fit(with_no_spring, numbers):
        arr += get_arrangements(with_no_spring, numbers)

    return arr


def find_arrangements(line: str):
    splitted = line.split(' ')
    return get_arrangements(splitted[0], [int(n) for n in splitted[1].split(',')])


def solve(filename):
    with (open(filename) as file):
        lines = file.read().splitlines()
        result = 0
        for line in lines:
            arr = find_arrangements(line)
            print(arr, line)
            result += arr
        print(result)


if __name__ == '__main__':
    solve('test_input') # 21
    #solve('input') # 7251
