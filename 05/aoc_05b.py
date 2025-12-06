from pathlib import Path

input_file = Path('input.txt')
# input_file = Path('test.txt')

with open(input_file, 'r') as f:
    # Read fresh ranges
    fresh_ranges = set()
    while input_line := f.readline().strip():
        start, end = map(int, input_line.split('-'))
        fresh_ranges.add((start, end))

sorted_ranges = sorted(fresh_ranges)

start_val, end_val = sorted_ranges[0]
merged_ranges = []
for range in sorted_ranges[1:]:
    this_start, this_end = range
    if this_start <= (end_val + 1):
        end_val = max(end_val, this_end)
    else:
        merged_ranges.append((start_val, end_val))
        start_val, end_val = this_start, this_end
merged_ranges.append((start_val, end_val))

fresh_count = sum((end - start + 1) for start, end in merged_ranges)
print(f'Fresh count: {fresh_count}')
