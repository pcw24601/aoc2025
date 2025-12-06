from pathlib import Path

input_file = Path('input.txt')
# input_file = Path('test.txt')

with open(input_file, 'r') as f:
    input_line = f.readline().strip()


def parse_range(range_str):
    parts = range_str.split('-')
    return int(parts[0]), int(parts[1])


def parse_line(line):
    line_parts = line.split(',')
    parsed_ranges = [parse_range(part) for part in line_parts]
    return parsed_ranges


parsed_ranges = parse_line(input_line)


def count_invalid(id_range):
    start, end = id_range
    invalid_values = set()

    repeating_number = 1

    while True:
        num_repeats = 2
        while True:
            possible_invalid_number = int(str(repeating_number) * num_repeats)
            if possible_invalid_number > end:
                break
            if possible_invalid_number >= start:
                # print(f"Found invalid number: {possible_invalid_number}")
                invalid_values.add(possible_invalid_number)
            num_repeats += 1
        repeating_number += 1
        if repeating_number > int(str(end)[:(len(str(end)) +1) // 2]):
            break

    return invalid_values


total = 0
for id_range in parsed_ranges:
    # print(id_range)
    total += sum(count_invalid(id_range))

print(total)

