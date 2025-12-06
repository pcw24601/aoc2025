from pathlib import Path

input_file = Path('input.txt')
# input_file = Path('test.txt')

with open(input_file, 'r') as f:
    input_lines = [line.strip() for line in f.readlines()]

def max_joltage(battery_string):
    joltage_str = ''
    start_idx = 0
    for digit_num in range(1, 13):
        try:
            this_digit = max(int(digit) for digit in battery_string[start_idx:digit_num-12])
        except ValueError:
            this_digit = max(int(digit) for digit in battery_string[start_idx:])
        joltage_str += str(this_digit)
        for idx, digit in enumerate(battery_string[start_idx:digit_num-12:]):
            if int(digit) == this_digit:
                start_idx += idx + 1
                break
    joltage = int(joltage_str)
    # print(joltage)
    return joltage


total_joltage = sum((max_joltage(line) for line in input_lines))
print(total_joltage)
