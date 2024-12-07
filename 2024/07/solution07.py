def split_line(line: str):
    [value, numbers] = line.split(":")
    numbers = numbers.split()
    return int(value), list(map(int, numbers))


def is_valid_1(value, numbers):
    if len(numbers) == 1:
        if value == numbers[0]:
            return True
        else:
            return False
    if value % numbers[-1] == 0:
        if is_valid_1(value / numbers[-1], numbers[:-1]):
            return True
    return is_valid_1(value - numbers[-1], numbers[:-1])


def is_valid_2(value, numbers):
    if len(numbers) == 1:
        if value == numbers[0]:
            return True
        else:
            return False

    last_number = numbers[-1]
    # *
    if value % last_number == 0:
        if is_valid_2(value / last_number, numbers[:-1]):
            return True

    # ||
    mul = 10 ** len(str(last_number))
    if (value - last_number) % mul == 0:
        if is_valid_2((value - last_number) / mul, numbers[:-1]):
            return True
    # +
    return is_valid_2(value - last_number, numbers[:-1])


def solve(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()
        pi = [split_line(line) for line in lines]

        print(sum([value for (value, numbers) in pi if is_valid_1(value, numbers)]))
        print(sum([value for (value, numbers) in pi if is_valid_2(value, numbers)]))


if __name__ == '__main__':
    solve('test_input')  # 3749, 11387
    solve('input')  # 14711933466277, 286580387663654
