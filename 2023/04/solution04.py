import math
import re


def get_numbers(str):
    return [int(n) for n in re.findall('[\d]+', str)]


def cnt_matching_cards(line):
    numbers = line.split(':')[1]
    numbers_splitted = numbers.split('|')
    winning_numbers = get_numbers(numbers_splitted[0])
    owned_numbers = get_numbers(numbers_splitted[1])
    return sum([number in winning_numbers for number in owned_numbers])


def get_points(line):
    n = cnt_matching_cards(line)
    if n == 0:
        return 0
    return math.pow(2, (n - 1))


def solve_a(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        solution = sum([get_points(line) for line in lines])
        print(filename, solution)


def solve_b(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        cards = dict([(i, 1) for i in range(len(lines))])
        for idx, line in enumerate(lines):
            n = cnt_matching_cards(line)
            for i in range(idx + 1, idx + n + 1):
                cards[i] += cards[idx]
        print(cards)
        print(sum(cards.values()))


if __name__ == '__main__':
    solve_a('test_input')
    solve_a('input')

    solve_b('test_input')
    solve_b('input')
