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
santa_x = 500
santa_y = 500
robot_x = 500
robot_y = 500
grid[santa_x, santa_y] = 1

for i, direction in enumerate(directions):
    delta_x, delta_y = index_delta[direction]
    if verbose:
        print("direction:", direction)
        print("delta_x:", delta_x)
        print("delta_y", delta_y)
    if (i % 2) == 0:
        santa_x += delta_x
        santa_y += delta_y
        grid[santa_x, santa_y] += 1
    else:
        robot_x += delta_x
        robot_y += delta_y
        grid[robot_x, robot_y] += 1


print("Unique houses:", len(np.nonzero(grid)[0]))
