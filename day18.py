from __future__ import print_function

import numpy as np
from scipy.ndimage import generic_filter
import scipy.ndimage as ndimage

verbose = False


def state_of_light(neighbors):
    light = neighbors[4]
    on = np.sum(neighbors)
    if light:  # light is on
        if on == 3 or on == 4:  # 2 or 3 neighbors plus itself
            return 1
        else:
            return 0
    else:   # light is off
        if on == 3:
            return 1
        else:
            return 0


def print_grid(grid):
    for row in grid:
        print(''.join([['.', '#'][i] for i in row]))


def take_steps(grid, steps, partb=False):
    if verbose:
        print("Initial Grid")
        print_grid(grid)
    for i in range(steps):
        new_grid = generic_filter(
            grid, state_of_light, size=3, mode='constant')
        if partb:
            new_grid[0, 0] = 1
            new_grid[0, -1] = 1
            new_grid[-1, 0] = 1
            new_grid[-1, -1] = 1
        if verbose:
            print()
            print("After step", i+1)
            print_grid(new_grid)
        grid = new_grid
    return grid


# Example
example_grid = np.array([
    [0, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 0]])
grid = take_steps(example_grid, 4)
print(np.sum(grid))

input_grid = np.ones((100, 100), dtype='int')
for row_num, line in enumerate(open('inputs/input18.txt')):
    row = [{'#': 1, '.': 0}[i] for i in line.strip()]
    input_grid[row_num, :] = row

# part a
grid = take_steps(input_grid, 100)
print(np.sum(grid))

# part b
grid = take_steps(input_grid, 100, partb=True)
print(np.sum(grid))
