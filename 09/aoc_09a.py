from itertools import combinations
from pathlib import Path
from collections import namedtuple

input_file = Path('input.txt')
# input_file = Path('test.txt')

with open(input_file, 'r') as f:
    input_lines = [line.strip('\n') for line in f.readlines()]

Tile = namedtuple('Tile', ['x', 'y'])

tiles = set()


def area(tile1, tile2):
    return ((abs(tile1.x - tile2.x) + 1)
            * (abs(tile1.y - tile2.y) + 1))


for line in input_lines:
    parts = line.split(',')
    tile = Tile(int(parts[0]), int(parts[1]))
    tiles.add(tile)

max_area = 0
for tile1, tile2 in combinations(tiles, 2):
    max_area = max(max_area, area(tile1, tile2))

print(max_area)
