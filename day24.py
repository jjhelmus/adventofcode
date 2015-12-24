from __future__ import print_function
import itertools

import numpy as np

numbers = [int(l) for l in open('inputs/input24.txt')]
goal = int(sum(numbers) / 3)

# search for sets of 5 presents which sum to goal (none exist)
for group in itertools.combinations(numbers, 5):
    if sum(group) == goal:
        print(group)

# no sets of 5 presents exist so search for set of 6
min_quantum = 9999999999999
for group in itertools.combinations(numbers, 6):
    if sum(group) == goal:
        min_quantum = min(np.prod(group), min_quantum)
print(min_quantum)

# part b
goal_b = int(sum(numbers) / 4)

for group in itertools.combinations(numbers, 4):
    if sum(group) == goal_b:
        print(group)

# search of sets of 5 after checking for sets of 4
min_quantum = 9999999999999
for group in itertools.combinations(numbers, 5):
    if sum(group) == goal_b:
        min_quantum = min(np.prod(group), min_quantum)
print(min_quantum)
