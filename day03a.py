from __future__ import print_function

import numpy as np

verbose = False

with open('inputs/input03.txt') as f:
    directions = f.read().strip()


index_delta = {
    '^': (0, 1),
    'v': (0, -1),
    '>': (1, 0),
    '<': (-1, 0),
}

grid = np.zeros((1000, 1000), dtype='int32')
x = 500
y = 500
grid[x, y] = 1

for direction in directions:
    delta_x, delta_y = index_delta[direction]
    if verbose:
        print("direction:", direction)
        print("delta_x:", delta_x)
        print("delta_y", delta_y)
    x += delta_x
    y += delta_y
    grid[x, y] += 1

print("Unique houses:", len(np.nonzero(grid)[0]))
