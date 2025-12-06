def parse_input(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()
        return [[int(n) for n in line.strip()] for line in lines]


def find_joltage(bank: list[int], length: int):
    result = 0
    for i in range(length, 0, -1):
        digit = max(bank[:len(bank) - i + 1])
        pos = bank.index(digit)
        bank = bank[pos + 1:]
        result = 10 * result + digit
    return result


def solve(filename: str, length: int):
    banks = parse_input(filename)
    result = 0
    for bank in banks:
        result += find_joltage(bank, length)
    print(result)
    return result


if __name__ == '__main__':
    assert solve('test_input', 2) == 357
    assert solve('input', 2) == 17493
    assert solve('test_input', 12) == 3121910778619
    assert solve('input', 12) == 173685428989126
