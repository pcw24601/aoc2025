from pathlib import Path

input_file = Path('input.txt')
# input_file = Path('test.txt')

with open(input_file, 'r') as f:
    input_lines = [line.strip() for line in f.readlines()]


def movable_roll(input_lines, row, col):
    max_row = len(input_lines)
    max_col = len(input_lines[0])
    point_value = input_lines[row][col]
    if point_value != '@':
        return 0
    start_row = (row - 1) if row > 0 else row
    start_col = (col - 1) if col > 0 else col
    end_row = (row + 1) if row < (max_row - 1) else row
    end_col = (col + 1) if col < (max_col - 1) else col

    conv_score = 0
    for r in range(start_row, end_row + 1):
        for c in range(start_col, end_col + 1):
            if (r == row) and (c == col):
                continue
            conv_score += (input_lines[r][c] == '@')

    return conv_score < 4

total_movable = 0
for r in range(len(input_lines)):
    for c in range(len(input_lines[0])):
        total_movable += movable_roll(input_lines, r, c)

print(total_movable)