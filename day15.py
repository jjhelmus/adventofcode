from __future__ import print_function
import numpy as np

c0prop = np.array([4, -2,  0, 0, 5])  # Frosting
c1prop = np.array([0,  5, -1, 0, 8])  # Candy
c2prop = np.array([-1, 0,  5, 0, 6])  # Butterscotch
c3prop = np.array([0,  0, -2, 2, 1])  # Sugar

max_score = 0
max_500_score = 0
for c0 in range(101):
    for c1 in range(0, 101-c0):
        remain = 100 - c0 - c1
        c2 = np.arange(remain + 1)
        c3 = remain - c2

        sums_of_prop = (c0*c0prop + c1*c1prop +
                        np.outer(c2, c2prop) + np.outer(c3, c3prop))
        calories = sums_of_prop[:, -1]
        sums_of_prop = sums_of_prop[:, :-1]  # remove calories
        sums_of_prop[sums_of_prop < 0] = 0   # replace negatives with zeros

        max_score = max(np.prod(sums_of_prop, axis=1).max(), max_score)

        # part B, find all the cookies with 500 calories
        cal_500_prop = sums_of_prop[calories == 500]
        if len(cal_500_prop) == 0:
            continue
        max_500_score = max(np.prod(cal_500_prop, axis=1).max(), max_500_score)

print(max_score)
print(max_500_score)
