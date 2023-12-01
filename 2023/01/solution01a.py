import re

pattern = re.compile(r'[\d]')
sum = 0
with open('input', 'r') as file:
    for line in file:
        digits = pattern.findall(line)
        first_digit = int(digits[0])
        last_digit = int(digits[-1])
        two_digit_number = 10 * first_digit + last_digit
        sum += two_digit_number
        print(f"{first_digit}, {last_digit}, {line}")

print(sum)
