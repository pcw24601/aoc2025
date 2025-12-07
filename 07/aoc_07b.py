from functools import lru_cache
from pathlib import Path

input_file = Path('input.txt')
# input_file = Path('test.txt')

with open(input_file, 'r') as f:
    input_lines = [line.strip('\n') for line in f.readlines()]

# Find initial taychon beam
initial_position = input_lines[0].find('S')
input_lines = input_lines[1:]

@lru_cache()
def number_paths(position, line_index):
    try:
        if input_lines[line_index][position] == '^':
            return (number_paths(position - 1, line_index + 1) +
                    number_paths(position + 1, line_index + 1))
        elif input_lines[line_index][position] == '.':
            return number_paths(position, line_index + 1)
        else:
            raise ValueError(f"Unexpected character '{input_lines[line_index][position]}' at position {position}")
    except IndexError:
        return 1  # end of path

total_paths = number_paths(initial_position, 0)

print(total_paths)