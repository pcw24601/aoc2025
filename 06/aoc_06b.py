from pathlib import Path
import numpy as np

input_file = Path('input.txt')
# input_file = Path('test.txt')

with open(input_file, 'r') as f:
    input_lines = [line.strip('\n') for line in f.readlines()]

operators = input_lines[-1]
numbers_lines = input_lines[:-1]

max_line_len = max([len(line) for line in numbers_lines])

all_problems = []
this_problem = []
for i in range(max_line_len):
    digit_list = []
    try:
        for j in range(len(numbers_lines)):
            try:
                digit_list.append(numbers_lines[j][i])
            except IndexError:
                digit_list.append(' ')
        this_number = int(''.join(digit_list))
        this_problem.append(this_number)
    except ValueError:
        all_problems.append(this_problem)
        this_problem = []
all_problems.append(this_problem)
# print(all_problems)

def get_operator(operators):
    for char in operators:
        if char == '+':
            yield np.sum
        if char == '*':
            yield np.prod


total = 0
operator_gen = get_operator(operators)
for line in all_problems:
    op = next(operator_gen)
    result = op(line)
    total += result
    # print(result)

print(total)