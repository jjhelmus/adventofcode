from __future__ import print_function


def is_nice(string):

    # Does NOT contain strings
    for s in ['ab', 'cd', 'pq', 'xy']:
        if s in string:
            return False

    # contains at least three vowels
    vowels = (string.count('a') + string.count('e') + string.count('i') +
              string.count('o') + string.count('u'))
    if vowels < 3:
        return False

    # contains at least one letter that appears twice in a row
    if any([string[i] == string[i+1] for i in range(len(string)-1)]):
        return True
    else:
        return False

test_strings = ['ugknbfddgicrmopn', 'aaa', 'jchzalrnumimnmhp',
                'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb']
for test_string in test_strings:
    print(test_string, ":", is_nice(test_string))

f = open('inputs/input05.txt')
nice_strings = 0
for line in f:
    if is_nice(line.strip()):
        nice_strings += 1
print("Nice strings:", nice_strings)
f.close()
