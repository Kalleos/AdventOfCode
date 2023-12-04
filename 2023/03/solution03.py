import math
import re


def get_all_numbers(matrix):
    numbers = []
    for row_nr, row in enumerate(matrix):
        for m in re.finditer(r'\d+', row):
            numbers.append((row_nr, m.start(), m.group()))
    return numbers


def contains_symbol(str):
    return True if re.search(r'[^\d^\\.]', str) else False


def is_part_number(number_def, matrix):
    (row, col, number) = number_def
    row_length = len(matrix[row])
    if row > 0 and contains_symbol(matrix[row - 1][max(0, col - 1):min(row_length, col + len(number) + 1)]):
        return True
    if row < len(matrix) - 1 and contains_symbol(
            matrix[row + 1][max(0, col - 1):min(row_length, col + len(number) + 1)]):
        return True
    if col > 0 and contains_symbol(matrix[row][col - 1]):
        return True
    if col + len(number) + 1 <= row_length and contains_symbol(matrix[row][col + len(number)]):
        return True
    return False


def is_adjacent(f_row, f_col, part_number):
    (row, col, number) = part_number
    if f_row == row - 1 and col - 1 <= f_col <= col + len(number):
        return True
    if f_row == row + 1 and col - 1 <= f_col <= col + len(number):
        return True
    if f_row == row and col - 1 == f_col:
        return True
    if f_row == row and col + len(number) == f_col:
        return True
    return False


def get_gear_ratio(gear_row, gear_col, part_numbers):
    adjacent_part_numbers = [int(number) for (row, col, number) in part_numbers if
                             is_adjacent(gear_row, gear_col, (row, col, number))]
    # print(gear_row, gear_col, adjacent_part_numbers)
    if len(adjacent_part_numbers) == 2:
        return math.prod(adjacent_part_numbers)
    return 0


if __name__ == '__main__':
    with open('input', 'r') as file:
        matrix = file.read().splitlines()

    numbers = get_all_numbers(matrix)
    # print(numbers)
    part_numbers = [number for number in numbers if is_part_number(number, matrix)]
    # print(part_numbers)
    sol_sum = sum([int(number) for (_, _, number) in part_numbers])
    print(sol_sum)  # 546563

    sum_gear_ratio = 0
    for (row_nr, row) in enumerate(matrix):
        for m in re.finditer(r'[\\*]', row):
            start = m.start()
            sum_gear_ratio += get_gear_ratio(row_nr, start, part_numbers)

    print(sum_gear_ratio)  # 91031374
