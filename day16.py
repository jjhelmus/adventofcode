from __future__ import print_function
import re
from operator import ge, le

KNOWN = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

SPECIAL = {'cats': le, 'trees': le, 'pomeranians': ge, 'goldfish': ge}


def is_real_aunt_parta(things, values):
    for thing, value in zip(things, values):
        if KNOWN[thing] != int(value):
            return False
    return True


def is_real_aunt_partb(things, values):

    for special_thing, compare in SPECIAL.items():
        if special_thing in things:
            number_of_things = int(values.pop(things.index(special_thing)))
            things.remove(special_thing)
            if compare(number_of_things, KNOWN[special_thing]):
                return False

    return is_real_aunt_parta(things, values)


pattern = 'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)'
for match in re.findall(pattern, open('inputs/input16.txt').read()):
    num = match[0]
    things = list(match[1::2])
    values = list(match[2::2])

    if is_real_aunt_parta(things, values):
        print("Part A:", num)

    if is_real_aunt_partb(things, values):
        print("Part B", num)
