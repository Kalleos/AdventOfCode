import re

digit_map = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

pattern = re.compile(r'[\d]|zero|one|two|three|four|five|six|seven|eight|nine')


def find_last_digit(line: str):
    pos = len(line) - 1
    while pos >= 0:
        m = pattern.match(line, pos)
        if m:
            return m.group()
        pos -= 1


if __name__ == '__main__':
    sum = 0
    with open('input', 'r') as file:
        for line in file:
            first_digit = digit_map[pattern.search(line).group()]
            last_digit = digit_map[find_last_digit(line)]
            two_digit_number = 10 * first_digit + last_digit
            sum += two_digit_number

    print(sum)  # 54985
