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
    invalid_values = []
    if start > end:
        print(f'Invalid range {start}-{end}')
        return invalid_values

    len_start = len(str(start))
    len_end = len(str(end))

    # numbers must be of even length, If odd length, truncate even range
    if len_start % 2:
        start = int('1' + '0' * (len_start))
    if len_end % 2:
        end = int('9' * (len_end-1))

    start_high = int(str(start)[:len(str(start))//2])
    end_high = int(str(end)[:len(str(end))//2])

    # print(f"Start: {start} (high: {start_high}, low: {start_low}), "
    #       f"End: {end} (high: {end_high}, low: {end_low})")

    for poss_invalid_high in range(start_high, end_high + 1):
        poss_invalid = int(str(poss_invalid_high) + str(poss_invalid_high))
        if start <= poss_invalid <= end:
            invalid_values.append(poss_invalid)
    return invalid_values

total = 0
for id_range in parsed_ranges:
    # print(count_invalid(id_range))
    total += sum(count_invalid(id_range))

print(total)

