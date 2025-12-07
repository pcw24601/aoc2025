from pathlib import Path

input_file = Path('input.txt')
# input_file = Path('test.txt')

with open(input_file, 'r') as f:
    input_lines = [line.strip('\n') for line in f.readlines()]

# Find initial taychon beam
taychon_positions = {input_lines[0].find('S')}
input_lines = input_lines[1:]
# print(taychon_positions)

split_count = 0
for line in input_lines:
    new_taychon_positions = set()
    for taychon_pos in taychon_positions:
        if line[taychon_pos] == '^':
            new_taychon_positions.add(taychon_pos - 1)
            new_taychon_positions.add(taychon_pos + 1)
            split_count += 1
        elif line[taychon_pos] == '.':
            new_taychon_positions.add(taychon_pos)
        else:
            raise ValueError(f"Unexpected character '{line[taychon_pos]}' at position {taychon_pos}")
    taychon_positions = new_taychon_positions
print(split_count)
