from __future__ import print_function

import numpy as np


def next_code(code):
    return code * 252533 % 33554393

# column and row for the input
column = 3083
row = 2978

# moving between column adds 2, 3, 4, ... to the code number
code_at_column_start = np.sum(np.arange(2, column + 1)) + 1
# moving down a column adds the column number, +1, +2 ...
code_number = code_at_column_start + np.sum(np.arange(column, column+row-1))

code = 20151125
for i in xrange(code_number - 1):
    code = next_code(code)
print(code)
