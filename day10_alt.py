from __future__ import print_function
from urllib2 import urlopen

# Since the input can be generated from a starting sequence of
# one of 2, 3, 4, ..., 9,  the number of digits follows OEIS A022471
seq = [l.split()[-1] for l in urlopen('http://oeis.org/A022471/b022471.txt')]
print(seq[seq.index(str(len('1113122113')))+40])
print(seq[seq.index(str(len('1113122113')))+50])
