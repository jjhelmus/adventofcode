from __future__ import print_function

import hashlib

puzzle_input = 'yzbqklnj'


def find_answer(secret_key):
    for i in xrange(10000000):
        message = secret_key + str(i)
        if hashlib.md5(message).hexdigest()[:5] == '00000':
            return i
    return None


def find_six_zeros(secret_key):
    for i in xrange(10000000):
        message = secret_key + str(i)
        if hashlib.md5(message).hexdigest()[:6] == '000000':
            return i
    return None

print('abcdef:', find_answer('abcdef'))
print('pqrstuv:', find_answer('pqrstuv'))
print('puzzle input:', find_answer(puzzle_input))
print('puzzle input:', find_six_zeros(puzzle_input))
