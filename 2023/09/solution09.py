def get_history(line):
    dreieck = []
    numbers = [int(n) for n in line.split(' ')]
    while not all([n == 0 for n in numbers]):
        dreieck.append(numbers)
        numbers = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
    dreieck.append(numbers)
    # print(dreieck)
    return sum([row[-1] for row in dreieck])


def solve(filename):
    with open(filename, 'r') as file:
        result = sum([get_history(line) for line in file.read().splitlines()])
        print(result)


if __name__ == '__main__':
    solve('test_input')
    solve('input')
