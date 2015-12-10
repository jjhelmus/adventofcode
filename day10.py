from __future__ import print_function
from itertools import groupby

s = '1113122113'
for i in range(40):
    s = ''.join([str(len(list(g)))+k for k, g in groupby(s)])
print(len(s))

# Part Two, 10 additional application
for i in range(10):
    s = ''.join([str(len(list(g)))+k for k, g in groupby(s)])
print(len(s))
