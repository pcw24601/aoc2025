from pathlib import Path

input_file = Path('input.txt')
# input_file = Path('test.txt')

with open(input_file, 'r') as f:
    input_lines = [line.strip() for line in f.readlines()]

current_pos = 50
zero_count = 0
for line in input_lines:
    dir = line[0]
    count = int(line[1:])
    if dir == 'R':
        current_pos += count
        while current_pos >= 100:
            current_pos -= 100
            zero_count += 1
    elif dir == 'L':
        current_pos -= count
        while current_pos < 0:
            current_pos += 100
            zero_count += 1

print(zero_count)
