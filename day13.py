from __future__ import print_function
import itertools

verbose = False

happiness = {}
people = set()

#f = open('inputs/input13_test.txt')
f = open('inputs/input13.txt')
for line in f:

    split_line = line.split()

    person1 = split_line[0]
    direction = split_line[2]
    amount = int(split_line[3])
    person2 = split_line[10][:-1]

    if verbose:
        print(person1, direction, amount, person2)

    people.add(person1)
    people.add(person2)

    if direction == 'lose':
        happiness[person1+person2] = -amount
    else:
        assert direction == 'gain'
        happiness[person1+person2] = amount
f.close()

if verbose:
    print(people)
    print(happiness)


def find_maximum_happiness(people, happiness):
    maximum_happiness = 0
    for arragement in itertools.permutations(people):
        happiness_gained = 0
        for person1, person2 in zip(arragement[:-1], arragement[1:]):
            happiness_gained += happiness[person1 + person2]
            happiness_gained += happiness[person2 + person1]
        # add happiness for first and last pair
        person1 = arragement[0]
        person2 = arragement[-1]
        happiness_gained += happiness[person1 + person2]
        happiness_gained += happiness[person2 + person1]
        maximum_happiness = max(maximum_happiness, happiness_gained)

        if verbose:
            print(arragement, happiness_gained)
    return maximum_happiness

print(find_maximum_happiness(people, happiness))

# part b
for person in people:
    happiness['Self' + person] = 0
    happiness[person + 'Self'] = 0
people.add('Self')
print(find_maximum_happiness(people, happiness))
