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


def find_last_digit(line: str, start):
    pos = start
    while pos >= 0:
        all_digits = pattern.findall(line, pos)
        if len(all_digits) > 1:
            print('something went wrong')
        if len(all_digits) == 1:
            return all_digits[0]
        pos -= 1


sum = 0
with open('input', 'r') as file:
    for line in file:
        digits = pattern.findall(line)
        first_digit = digit_map.get(digits[0])
        last_digit = digit_map.get(find_last_digit(line, len(line) - 1))
        two_digit_number = 10 * first_digit + last_digit
        sum += two_digit_number
        print(f"{first_digit}, {last_digit}, {line}")

print(sum)
