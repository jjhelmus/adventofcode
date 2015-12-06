from __future__ import print_function

import numpy as np

verbose = False

grid = np.zeros((1000, 1000), 'int32')

f = open('inputs/input06.txt')

for line in f:
    line = line.strip()
    lline = line.split()
    if verbose:
        print("line:", line)
        print("lline:", lline)

    # Turn on/off
    if lline[0] == 'turn':
        x1, y1 = lline[2].split(',')
        x2, y2 = lline[4].split(',')
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        if lline[1] == 'on':
            grid[x1:x2+1, y1:y2+1] = 1
        else:
            assert lline[1] == 'off'
            grid[x1:x2+1, y1:y2+1] = 0

    # Troggle
    else:
        assert lline[0] == 'toggle'
        x1, y1 = lline[1].split(',')
        x2, y2 = lline[3].split(',')
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        grid[x1:x2+1, y1:y2+1] = np.logical_not(grid[x1:x2+1, y1:y2+1])
    if verbose:
        print('x1, y1:', x1, y1)
        print('x2, y2:', x2, y2)
print(np.sum(grid))

f.close()

