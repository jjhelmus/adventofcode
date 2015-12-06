from __future__ import print_function


def is_nice(string):

    # repeats with exactly one letter between them
    if not any([string[i] == string[i+2] for i in range(len(string)-2)]):
        return False

    # pair appears at least twice
    if any([(string.count(string[i:i+2])>=2) for i in range(len(string)-2)]):
        return True
    return False

test_strings = [
    'qjhvhtzxzqqjkmpb',
    'xxyxx',
    'uurcxstgmygtbstg',
    'ieodomkazucvgmuy']

for test_string in test_strings:
    print(test_string, ":", is_nice(test_string))

f = open('inputs/input05.txt')
nice_strings = 0
for line in f:
    if is_nice(line.strip()):
        nice_strings += 1
print("Nice strings:", nice_strings)
f.close()
