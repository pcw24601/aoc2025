from pathlib import Path
from collections import namedtuple
import numpy as np

input_file = Path('input.txt')
num_connections = 1000
# input_file = Path('test.txt')
# num_connections = 10

with open(input_file, 'r') as f:
    input_lines = [line.strip('\n') for line in f.readlines()]

Jbox = namedtuple('Jbox', ['x', 'y', 'z'])
Wire = namedtuple('Wire', ['distance', 'jbox1', 'jbox2'])

jboxes = []
circuits = []
possible_wires = set()

def squared_distance(jbox1, jbox2):
    # no point in taking square root unless we need actual distance
    return ((jbox1.x - jbox2.x) ** 2 +
            (jbox1.y - jbox2.y) ** 2 +
            (jbox1.z - jbox2.z) ** 2)


for line in input_lines:
    parts = line.split(',')
    jbox = Jbox(int(parts[0]), int(parts[1]), int(parts[2]))
    jboxes.append(jbox)
    circuits.append([jbox])

for index_, jbox1 in enumerate(jboxes):
    for jbox2 in jboxes[index_ + 1:]:
        if jbox1 != jbox2:
            dist = squared_distance(jbox1, jbox2)
            possible_wires.add(Wire(dist, jbox1, jbox2))

possible_wires = sorted(possible_wires)

def join_circuits(wire):
    for index_, circuit in enumerate(circuits):
        if wire.jbox1 in circuit:
            circuit1_index = index_
        if wire.jbox2 in circuit:
            circuit2_index = index_
    if circuit1_index == circuit2_index:
        return  # no action, circuits already joined

    circuits[circuit1_index] += circuits[circuit2_index]
    del circuits[circuit2_index]

for wire in possible_wires[:num_connections]:
    join_circuits(wire)

circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
print(np.prod([len(circuit) for circuit in circuits[:3]]))
