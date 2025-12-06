from pathlib import Path
import numpy as np

input_file = Path('input.txt')
# input_file = Path('test.txt')

with open(input_file, 'r') as f:
    input_lines = [line.strip() for line in f.readlines()]

operators = input_lines[-1]
numbers_lines = input_lines[:-1]

numbers = []
for line in numbers_lines:
    number_line = []
    for num_str in line.split(' '):
        try:
            number_line.append(int(num_str))
        except ValueError:
            pass
    numbers.append(number_line)

# transpose numbers
transposed_numbers = []
for i in range(len(numbers[0])):
    transposed_numbers.append([numbers[j][i] for j in range(len(numbers))])
# print(transposed_numbers)

def get_operator(operators):
    for char in operators:
        if char == '+':
            yield np.sum
        if char == '*':
            yield np.prod

total = 0
operator_gen = get_operator(operators)
for line in transposed_numbers:
    op = next(operator_gen)
    result = op(line)
    total += result
    # print(result)

print(total)