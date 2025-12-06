from pathlib import Path

input_file = Path('input.txt')
# input_file = Path('test.txt')

with open(input_file, 'r') as f:
    # Read fresh ranges
    fresh_ranges = set()
    while input_line := f.readline().strip():
        start, end = map(int, input_line.split('-'))
        fresh_ranges.add((start, end))

    ingredients = set()
    while input_line := f.readline().strip():
        ingredients.add(int(input_line))

# print(f'Fresh ranges: {fresh_ranges}')
# print(f'Ingredients: {ingredients}')

fresh_count = 0
for ingredient in ingredients:
    for start, end in fresh_ranges:
        if start <= ingredient <= end:
            fresh_count += 1
            break
print(fresh_count)